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
