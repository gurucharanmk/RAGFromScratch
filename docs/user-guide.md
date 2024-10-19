# RAG System Usage Guide

## Overview
This document explains how to use the RAGFromScratch system, which combines document retrieval with language model generation to provide accurate, context-aware responses to questions.

## Basic Usage

### 1. Configure Components
```python
from src.config.model_config import OllamaConfig
from src.config.vector_db_config import FAISSConfig
from src.config.data_source_config import PDFConfig

ollama_config = OllamaConfig(llm_model="llama2")
faiss_config = FAISSConfig(index_path="./data/vector_store/vdb.index")
pdf_config = PDFConfig(pdf_path="./data/source/document.pdf")
```

### 2. Initialize RAG System
```python
from src.rag_system import RAGSystem

rag = RAGSystem(ollama_config, faiss_config, pdf_config)
```

### 3. Index Documents
```python
rag.index_data()
```

### 4. Query the System
```python
response = rag.query("Your question here")
print(response)
```

## Configuration Options

### Data Sources
- PDF files (PDFConfig)
  - `pdf_path`: Path to PDF file

### Language Models
- Ollama (OllamaConfig)
  - `llm_model`: Model name (e.g., "llama2")

### Vector Databases
- FAISS (FAISSConfig)
  - `index_path`: Path to store/load FAISS index

## Support and Resources

- Ollama Documentation: [ollama.ai/docs](https://ollama.ai/docs)
- FAISS Documentation: [faiss.ai](https://faiss.ai/)

## License
[MIT](LICENSE.md)