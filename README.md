# Offline PDF RAG System

**A fully offline Retrieval-Augmented Generation (RAG) system for PDFs.** Query your documents locally without sending data online. Works with local embeddings and optionally integrates any locally installed LLM.

---

## ⚡ Features

- **Offline by design**: All PDFs, embeddings, and models stay on your laptop.  
- **Local PDF ingestion**: Select a folder of PDFs to process.  
- **Text extraction & cleaning**: Converts PDFs into clean, searchable text.  
- **Chunking**: Splits large texts into manageable overlapping chunks.  
- **Embeddings generation**: Uses `SentenceTransformers` for semantic search.  
- **Persistent local storage**: ChromaDB stores embeddings and metadata locally.  
- **Interactive Q&A**: Ask questions via terminal and retrieve top relevant chunks.  
- **Optional local LLM integration**: Use GPT4All, Ollama, or HuggingFace models for natural language answers.  
- **Modular & flexible**: Add new PDFs, embeddings, or LLMs without changing core code.  

---

## 🛠 Installation

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd <repo-folder>
```
Install dependencies:

```bash

pip install -r requirements.txt
```
Dependencies explained:

PyPDF2: PDF reading and text extraction.

langchain: Text splitting and chunking.

sentence-transformers + torch: Generate embeddings for chunks.

chromadb: Local vector database for persistent embeddings.

pickle5: Save/load embeddings cache.

Optional: gpt4all or ollama-client for local LLM integration.

##📂 Usage

Run the offline RAG system:
```bash

python local.py
```
Enter the path to your PDF folder when prompted.

The system will extract, chunk, and embed your PDFs automatically.

Ask questions in the terminal and see the top retrieved chunks.

Optional: Download HuggingFace models for local LLM:
```bash

python download_hf_models.py
```
Downloads LLaMA 2, MPT-7B, Falcon-7B models into local_hf_models/.

Models can be loaded offline into your RAG system for generating answers.

##🧩 How It Works

PDF Ingestion: User selects a folder of PDFs.

Text Extraction: PDFs are read, cleaned, and concatenated.

Chunking: Text split into overlapping chunks for semantic search.

Embeddings: Chunks converted to vectors using SentenceTransformer.

Vector Storage: Stored in local ChromaDB for fast retrieval.

Query & Retrieve: User enters a query; system finds top matching chunks.

Local LLM (optional): Retrieved chunks passed to a local model for generating human-like answers.

##💡 Why This Is Cool

100% offline — data never leaves your laptop.

Learn & experiment — see how embeddings and tokenizers work.

Flexible — add PDFs or LLMs easily.

Terminal-friendly — minimal setup, no GUI required.

##🚀 Next Steps

Integrate your preferred local LLM for natural language answers.

Add dynamic updates to index new PDFs without restarting the system.

Experiment with different embeddings models for better retrieval quality.

Tip: Start with the terminal interface to understand how embeddings and retrieval work. Once comfortable, hook up any local LLM to generate answers entirely offline.
