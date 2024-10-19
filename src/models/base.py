from abc import ABC, abstractmethod
from typing import List


class LanguageModel(ABC):
    """Abstract base class for language models."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate text based on the given prompt.

        Examples:
            >>> model.generate("Your question here")
            'LLM response here.'
        """
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def get_embeddings(self, text: str) -> List[float]:
        """
        Get embeddings for the given text.

        Examples:
            >>> embeddings = model.get_embeddings("Hello, world!")
            >>> print(len(embeddings))
            768
        """
        raise NotImplementedError  # pragma: no cover
