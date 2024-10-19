from typing import List
from .config.model_config import ModelConfig, OllamaConfig
from .config.vector_db_config import VectorDBConfig, FAISSConfig
from .config.data_source_config import DataSourceConfig, PDFConfig
from .models.base import LanguageModel
from .models.ollama_model import OllamaModel
from .vector_db.base import VectorDB
from .vector_db.faiss_db import FAISSVectorDB
from .data_source.base import DataSource
from .data_source.pdf_source import PDFDataSource
from .text_splitter.recursive_splitter import RecursiveTextSplitter
from .prompt import Prompt


class RAGSystem:
    """
    Main class for the RAG system.

    Examples:
        >>> ollama_config = OllamaConfig(model_name="llama2")
        >>> faiss_config = FAISSConfig(index_path="/path/to/faiss/index")
        >>> pdf_config = PDFConfig(pdf_path="/path/to/documents.pdf")
        >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
        >>> rag.index_data()
        >>> response = rag.query("Your question here")
        >>> print(response)
        'RAG response here'
    """

    def __init__(
        self,
        model_config: ModelConfig,
        vector_db_config: VectorDBConfig,
        data_source_config: DataSourceConfig,
    ) -> None:
        """
        Initialize RAG system.

        Args:
            model_config: Configuration for the language model
            vector_db_config: Configuration for the vector database
            data_source_config: Configuration for the data source

        Returns:
            None

        Examples:
            >>> ollama_config = OllamaConfig(model_name="llama2")
            >>> faiss_config = FAISSConfig(index_path="/path/to/faiss/index")
            >>> pdf_config = PDFConfig(pdf_path="/path/to/documents.pdf")
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
        """
        self.model: LanguageModel = self._initialize_model(model_config)
        self.vector_db: VectorDB = self._initialize_vector_db(vector_db_config)
        self.data_source: DataSource = self._initialize_data_source(data_source_config)
        self.text_splitter: RecursiveTextSplitter = RecursiveTextSplitter()

    def _initialize_model(self, config: ModelConfig) -> LanguageModel:
        """
        Initialize language model based on configuration.

        Args:
            config: Model configuration object

        Returns:
            Initialized language model instance

        Examples:
            >>> ollama_config = OllamaConfig(model_name="llama2")
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
            >>> model = rag._initialize_model(ollama_config)
            >>> isinstance(model, OllamaModel)
            True
        """
        if isinstance(config, OllamaConfig):
            return OllamaModel(config)
        raise ValueError("Unsupported model configuration")

    def _initialize_vector_db(self, config: VectorDBConfig) -> VectorDB:
        """
        Initialize vector database based on configuration.

        Args:
            config: Vector database configuration object

        Returns:
            Initialized vector database instance

        Examples:
            >>> faiss_config = FAISSConfig(index_path="/path/to/faiss/index")
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
            >>> vector_db = rag._initialize_vector_db(faiss_config)
            >>> isinstance(vector_db, FAISSVectorDB)
            True
        """
        if isinstance(config, FAISSConfig):
            return FAISSVectorDB(config)
        raise ValueError("Unsupported vector database configuration")

    def _initialize_data_source(self, config: DataSourceConfig) -> DataSource:
        """
        Initialize data source based on configuration.

        Args:
            config: Data source configuration object

        Returns:
            Initialized data source instance

        Examples:
            >>> pdf_config = PDFConfig(pdf_path="/path/to/documents.pdf")
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
            >>> data_source = rag._initialize_data_source(pdf_config)
            >>> isinstance(data_source, PDFDataSource)
            True
        """
        if isinstance(config, PDFConfig):
            return PDFDataSource(config)
        raise ValueError("Unsupported data source configuration")

    def index_data(self) -> None:
        """
        Index data from the data source into the vector database.

        Args:


        Returns:
            None

        Examples:
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
            >>> rag.index_data()
            >>> # Check if vector_db has embeddings
            >>> len(rag.vector_db.get_all_embeddings()) > 0
            True
        """
        documents: List[str] = self.data_source.load_data()
        chunks: List[str] = []
        for doc in documents:
            chunks.extend(self.text_splitter.split_text(doc))
        embeddings: List[List[float]] = [
            self.model.get_embeddings(chunk) for chunk in chunks
        ]
        metadata: List[dict[str, str]] = [{"text": chunk} for chunk in chunks]
        self.vector_db.add_embeddings(embeddings, metadata)

    def query(self, query: str, k: int = 5) -> str:
        """
        Process a query and return the response.

        Args:
            query: User question string
            k: Number of similar documents to retrieve

        Returns:
            Generated response string

        Examples:
            >>> rag = RAGSystem(ollama_config, faiss_config, pdf_config)
            >>> rag.index_data()
            >>> response = rag.query("Your question here")
            >>> isinstance(response, str)
            True
            >>> len(response) > 0
            True
        """
        query_embedding: List[float] = self.model.get_embeddings(query)
        similar_docs: List[dict[str, str]] = self.vector_db.search(query_embedding, k)
        context: str = "\n".join([doc["text"] for doc in similar_docs])
        prompt: Prompt = Prompt(
            system_message="You are a helpful AI assistant. Use the following context to answer the human's question.",
            ai_message=f"Context: {context}",
            human_message=query,
        )
        return self.model.generate(prompt.construct_prompt())
