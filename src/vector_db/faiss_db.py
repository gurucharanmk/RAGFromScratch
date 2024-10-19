from typing import List, Dict, Any, Optional
import faiss
import numpy as np
from .base import VectorDB
from ..config.vector_db_config import FAISSConfig


class FAISSVectorDB(VectorDB):
    """
    FAISS implementation of VectorDB

    This class provides methods to add embeddings and search for similar embeddings using FAISS.

    Examples:
        >>> from ..config.vector_db_config import FAISSConfig
        >>> config = FAISSConfig(index_path="/path/to/faiss/index")
        >>> vector_db = FAISSVectorDB(config)
        >>> embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        >>> metadata = [{"text": "Hello"}, {"text": "World"}]
        >>> vector_db.add_embeddings(embeddings, metadata)
        >>> query_embedding = [0.1, 0.2, 0.3]
        >>> results = vector_db.search(query_embedding, k=1)
        >>> print(results)
        [{'distance': 0.0, 'index': 0, 'text': 'Hello'}]
    """

    def __init__(self, config: FAISSConfig) -> None:
        """
        Initialize FAISS vector database.

        Args:
            config (FAISSConfig): Configuration object for the FAISS vector database.

        Examples:
            >>> from ..config.vector_db_config import FAISSConfig
            >>> config = FAISSConfig(index_path="/path/to/faiss/index")
            >>> vector_db = FAISSVectorDB(config)
        """
        self.file_path: str = config.index_path
        self.index: Optional[faiss.Index] = None
        self.dimension: Optional[int] = None
        self.texts: List[str] = []

    '''
    def _load_or_create_index(self) -> None:
        """
        Load existing index or prepare for creating a new one.

        Examples:
            >>> vector_db = FAISSVectorDB(FAISSConfig(index_path="/path/to/faiss/index"))
            >>> vector_db._load_or_create_index()
        """
        if os.path.exists(self.file_path):
            self.index = faiss.read_index(self.file_path)
            print(f"Loaded existing index from {self.file_path}")
        else:
            print(
                f"Index file not found at {self.file_path}. It will be created when adding embeddings."
            )
    '''

    def add_embeddings(
        self, embeddings: List[List[float]], metadata: List[Dict[str, Any]]
    ) -> None:
        """
        Add embeddings to FAISS index.

        Args:
            embeddings (List[List[float]]): List of embedding vectors to add.
            metadata (List[Dict[str, Any]]): List of metadata dictionaries corresponding to the embeddings.

        Examples:
            >>> vector_db = FAISSVectorDB(FAISSConfig(index_path="/path/to/faiss/index"))
            >>> embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
            >>> metadata = [{"text": "Hello"}, {"text": "World"}]
            >>> vector_db.add_embeddings(embeddings, metadata)
        """
        embeddings_array: np.ndarray = np.array(embeddings).astype("float32")

        if self.index is None:
            self.dimension = embeddings_array.shape[1]
            self.index = faiss.IndexFlatL2(self.dimension)
            print(f"Created new index with dimension {self.dimension}")

        self.index.add(embeddings_array)
        self.texts.extend([m["text"] for m in metadata])  # Store the text content

        # Save the updated index
        faiss.write_index(self.index, self.file_path)
        print(f"Saved index to {self.file_path}")

    def search(self, query_embedding: List[float], k: int) -> List[Dict[str, Any]]:
        """
        Search for similar embeddings in FAISS index.

        Args:
            query_embedding (List[float]): The query embedding vector.
            k (int): The number of nearest neighbors to return.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing search results.

        Examples:
            >>> vector_db = FAISSVectorDB(FAISSConfig(index_path="/path/to/faiss/index"))
            >>> query_embedding = [0.1, 0.2, 0.3]
            >>> results = vector_db.search(query_embedding, k=1)
            >>> print(results)
            [{'distance': 0.0, 'index': 0, 'text': 'Hello'}]
        """
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [
            {
                "distance": float(distances[0][i]),
                "index": int(indices[0][i]),
                "text": self.texts[indices[0][i]],
            }
            for i in range(k)
        ]
