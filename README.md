# Offline-RAG-System-for-PDFs
A fully offline Retrieval-Augmented Generation (RAG) system that allows you to query your PDFs and retrieve relevant information, powered by local embeddings and optional local LLMs.
Offline RAG System for PDFs

This project is designed to run entirely on your machine — no internet required after setup. All PDFs, embeddings, and models stay local, so your data never leaves your laptop.

⚡ Key Features

Local PDF ingestion: Select a folder of PDFs to process and index.

Automatic text extraction & chunking: Converts PDFs into text chunks for better retrieval.

Embeddings generation: Uses SentenceTransformers to generate embeddings for efficient similarity search.

Persistent local storage: Embeddings are cached and stored in ChromaDB locally.

Interactive terminal Q&A: Ask questions in a terminal interface and retrieve top relevant chunks.

Optional local LLM integration: Hook in any locally installed model (e.g., Ollama, GPT4All, or HuggingFace models) to generate answers based on the retrieved context.

Fully modular: Add new PDFs, embeddings, or LLMs without changing the core code.

📂 How It Works

Select PDF folder: The system prompts you for a folder containing your PDFs.

Text extraction & cleaning: Each PDF is read, and text is cleaned to avoid formatting issues.

Chunking: Text is split into overlapping chunks to improve retrieval quality.

Embeddings generation: Chunks are converted into vector embeddings using a SentenceTransformer model.

ChromaDB storage: Embeddings and metadata are stored locally for persistent similarity search.

Interactive Q&A:

Type a query in the terminal.

The system retrieves the top chunks from your PDFs.

Optional: Pass retrieved chunks to a local LLM for a natural language answer.

⚙️ Usage

Clone the repo:

git clone <your-repo-url>
cd <repo-folder>


Install dependencies:

pip install -r requirements.txt


Run the offline RAG system:

python local.py


Enter the PDF folder path when prompted.

Ask questions in the terminal.

See top chunks retrieved or integrate your local LLM for answers.

Optional: Download HuggingFace models for local LLM:

python download_hf_models.py


Downloads LLaMA 2, MPT-7B, Falcon-7B (can add more).

Saved models can be loaded offline into your RAG system.

🧩 Why This Is Cool

100% offline: No data leaks, ideal for sensitive documents.

Learn & experiment: See how embeddings and tokenizers work, then plug in any LLM.

Flexible & modular: Add new PDFs, models, or LLMs easily.

Terminal-friendly: Quick to run, no heavy frontend required.

🚀 Next Steps

Integrate local LLMs (Ollama, GPT4All, HuggingFace) for natural language answers.

Add a dynamic update feature to index new PDFs on the fly.

Experiment with different embeddings models for better retrieval.

Tip: Start with the terminal interface to explore how embeddings and RAG work. Then, plug in your favorite LLM to generate human-like answers from your PDFs entirely offline.
