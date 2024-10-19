# RAG From Scratch

## Introduction

RAG From Scratch is a modular framework for Retrieval-Augmented Generation (RAG), built entirely from the ground up for educational purposes. This project aims to provide a clear and comprehensive understanding of how RAG functions under the hood, making it an invaluable resource for students, researchers, and anyone interested in learning about document processing, embedding generation, and language model inference.

## Key Features

- **Built from Scratch**: Every component of the framework has been developed from the ground up, offering insights into the foundational elements of RAG.
- **Well-Commented Code**: The code is thoroughly commented with examples, making it easy to follow and understand the key concepts and processes.
- **Modular Design**: Extend the framework to support additional language models, vector databases, and data sources.
- **Versatile Data Handling**: Currently supports PDF files, with the flexibility to easily extend the framework to accommodate additional formats, including PowerPoint (PPT), plain text, and Excel (XLSX) files.
- **Customizable Splitting Strategies**: Experiment with different document splitting strategies to observe their effects on retrieval and generation.

## Components

### Data Sources
- Base class: `DataSource`
- Implementations:
  - `PDFDataSource`: Handles PDF document loading

### Language Models
- Base class: `LanguageModel`
- Implementations:
  - `OllamaModel`: Integration with Ollama models

### Vector Databases
- Base class: `VectorDB`
- Implementations:
  - `FAISSVectorDB`: FAISS-based vector storage

### Text Processing
- `RecursiveTextSplitter`: Chunks text into manageable segments
- `Prompt`: Structures interactions with the language model

## Architecture
1. Data ingestion via DataSource
2. Text splitting with RecursiveTextSplitter
3. Embedding generation using LanguageModel
4. Vector storage in VectorDB
5. Query processing through RAG pipeline

## API Reference

For detailed information about the system's components and their usage, check out our [API Reference](api-reference/index.md).

## Note

This project is not intended for production use. Instead, it serves as a practical platform for understanding the principles and processes involved in Retrieval-Augmented Generation. Dive in to explore and learn!


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.