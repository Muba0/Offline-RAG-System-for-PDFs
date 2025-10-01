import os
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# --------------------------
# Ask user for PDF folder
# --------------------------
PDF_FOLDER = input("📂 Enter the path to your PDF folder: ").strip()
while not os.path.isdir(PDF_FOLDER):
    PDF_FOLDER = input("❌ Folder not found. Enter a valid PDF folder path: ").strip()
print(f"✅ Using PDF folder: {PDF_FOLDER}")

# --------------------------
# Config
# --------------------------
EMBEDDING_FILE = "embeddings.pkl"
CHROMA_DB_DIR = "chroma_store"

# --------------------------
# STEP 1: Load PDFs from folder
# --------------------------
docs = []
for filename in os.listdir(PDF_FOLDER):
    if filename.endswith(".pdf"):
        filepath = os.path.join(PDF_FOLDER, filename)
        print(f"Processing: {filename}")

        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                cleaned = " ".join(page_text.splitlines())
                text += cleaned + " "

        docs.append({"content": text, "source": filename})

print(f"Extracted text from {len(docs)} PDFs.")

# --------------------------
# STEP 2: Chunking
# --------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = []
for doc in docs:
    for chunk in splitter.split_text(doc["content"]):
        chunks.append({"content": chunk, "source": doc["source"]})

print(f"Total chunks created: {len(chunks)}")

# --------------------------
# STEP 3: Embeddings (load or generate)
# --------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")
if os.path.exists(EMBEDDING_FILE):
    print("Loading embeddings from cache...")
    with open(EMBEDDING_FILE, "rb") as f:
        chunks = pickle.load(f)
else:
    print("Generating embeddings...")
    for chunk in chunks:
        chunk["embedding"] = model.encode(chunk["content"]).tolist()
    with open(EMBEDDING_FILE, "wb") as f:
        pickle.dump(chunks, f)
    print("Embeddings saved!")

# --------------------------
# STEP 4: Store in Chroma (local persistence)
# --------------------------
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection("pdfs")
if collection.count() == 0:  # only add once
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            embeddings=[chunk["embedding"]],
            documents=[chunk["content"]],
            metadatas=[{"source": chunk["source"]}],
        )
    print("All chunks stored in Chroma!")

# --------------------------
# STEP 5: Interactive Q&A Loop
# --------------------------
print("\n✅ System ready! Ask me anything about your PDFs.")
print("Type 'exit' to quit.\n")

while True:
    query = input("Your question: ")
    if query.lower() in ["exit", "quit", "bye"]:
        print("👋 Ending session. Bye!")
        break

    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=3)

    # Display top chunks
    print("\n--- Top Retrieved Chunks ---")
    for i, doc in enumerate(results["documents"][0]):
        print(f"\nResult {i+1} (from {results['metadatas'][0][i]['source']}):\n")
        print(doc, "\n")
    print("-------------------\n")

    # --------------------------
    # Local LLM integration (optional)
    # --------------------------
    docs_context = "\n\n".join(results["documents"][0])
    prompt = f"""
    Context from PDFs:
    {docs_context}

    Question: {query}
    Answer based only on the context above:
    """

    # === Example: GPT4All ===
    # from gpt4all import GPT4All
    # model_gpt = GPT4All("gpt4all-lora-quantized.bin")  # your local model path
    # response = model_gpt.generate(prompt)
    # print("\n💡 LLM Answer:\n", response)

    # === Example: Ollama ===
    # import subprocess
    # response = subprocess.run(
    #     ["ollama", "generate", "llama2", prompt],
    #     capture_output=True,
    #     text=True
    # )
    # print("\n💡 LLM Answer:\n", response.stdout)

    # If not using local LLM, you can just see the chunks
    print("💡 Local LLM integration placeholder (uncomment code above to enable).")
