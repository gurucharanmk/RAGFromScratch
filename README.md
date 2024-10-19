# RAG From Scratch

## Introduction

RAG From Scratch is a modular framework for Retrieval-Augmented Generation (RAG), built entirely from the ground up for educational purposes. This project aims to provide a clear and comprehensive understanding of how RAG functions under the hood, making it an invaluable resource for students, researchers, and anyone interested in learning about document processing, embedding generation, and language model inference.

## Key Features

- **Built from Scratch**: Every component of the framework has been developed from the ground up, offering insights into the foundational elements of RAG.
- **Well-Commented Code**: The code is thoroughly commented with examples, making it easy to follow and understand the key concepts and processes.
- **Modular Design**: Extend the framework to support additional language models, vector databases, and data sources.
- **Versatile Data Handling**: Currently supports PDF files, with the flexibility to easily extend the framework to accommodate additional formats, including PowerPoint (PPT), plain text, and Excel (XLSX) files.
- **Customizable Splitting Strategies**: Experiment with different document splitting strategies to observe their effects on retrieval and generation.

## Features
- Modular architecture with support for multiple:
  - Data sources (PDF)
  - Language models (Ollama)
  - Vector databases (FAISS)
- Configurable text splitting
- Type-safe configuration using Pydantic
- Easy to extend with new components

## Quick Start

## Prerequisites

- **[Python 3.11 or higher](https://www.python.org)**
- **[pip](https://pypi.org/project/pip/)** (Python package installer)
- **[Make](https://www.gnu.org/software/make/)** (for running the Makefile)
- **[Poetry](https://python-poetry.org)** (for packaging and dependency management)

## Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gurucharanmk/RAGFromScratch
   cd RAGFromScratch
   ```

2. **Install dependencies and set up pre-commit hooks:**
   ```bash
   make install
   ```

3. **Set up Ollama:**
   ```bash
   make ollama
   ```

    ```python
    #main.py
    from src.config.model_config import OllamaConfig
    from src.config.vector_db_config import FAISSConfig
    from src.config.data_source_config import PDFConfig
    from src.rag_system import RAGSystem
    
    # Initialize configs
    ollama_config = OllamaConfig(llm_model="llama2")
    faiss_config = FAISSConfig(index_path="./data/vector_store/vdb.index")
    pdf_config = PDFConfig(pdf_path="./data/source/document.pdf")
    
    # Create and use RAG system
    rag = RAGSystem(ollama_config, faiss_config, pdf_config)
    rag.index_data()
    response = rag.query("Your question here")
    ```

4. **Run the initial data indexing:**
   ```bash
   python main.py  # Adjust this step if you need to run a specific script.
   ```

## Additional Commands

- **Run tests:**
  ```bash
  make test
  ```

- **Check coverage:**
  ```bash
  make coverage
  ```

- **Lint code:**
  ```bash
  make lint
  ```

- **Format code:**
  ```bash
  make format
  ```

- **Clean build artifacts:**
  ```bash
  make clean
  ```

- **Build documentation:**
  ```bash
  make docs
  ```

- **Serve documentation locally:**
  ```bash
  make docs-serve
  ```

- **Update dependencies:**
  ```bash
  make update
  ```

## Note

This project is not intended for production use. Instead, it serves as a practical platform for understanding the principles and processes involved in Retrieval-Augmented Generation. Dive in to explore and learn!