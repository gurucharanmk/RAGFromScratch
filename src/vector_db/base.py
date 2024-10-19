from abc import ABC, abstractmethod
from typing import List, Dict, Any


class VectorDB(ABC):
    """Abstract base class for vector databases."""

    @abstractmethod
    def add_embeddings(
        self, embeddings: List[List[float]], metadata: List[Dict[str, Any]]
    ) -> None:
        """
        Add embeddings to the vector database.

        Examples:
            >>> embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
            >>> metadata = [{"text": "Hello"}, {"text": "World"}]
            >>> vector_db.add_embeddings(embeddings, metadata)
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def search(self, query_embedding: List[float], k: int) -> List[Dict[str, Any]]:
        """
        Search for similar embeddings in the vector database.

        Examples:
            >>> query_embedding = [0.1, 0.2, 0.3]
            >>> results = vector_db.search(query_embedding, k=2)
            >>> print(results)
            [{'distance': 0.1, 'index': 0}, {'distance': 0.2, 'index': 1}]
        """
        raise NotImplementedError  # pragma: no cover
