# Installation Guide

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

4. **Run RAG:**
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


      ```bash
      python main.py  
      ```

## Additional Commands

- **Run unit tests:**
  ```bash
  make test
  ```

- **Check code coverage:**
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