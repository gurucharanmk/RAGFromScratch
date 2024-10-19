from abc import ABC, abstractmethod
from typing import List


class TextSplitter(ABC):
    """Abstract base class for text splitters."""

    @abstractmethod
    def split_text(self, text: str) -> List[str]:
        """
        Split the input text into chunks.

        Examples:
            >>> splitter = RecursiveTextSplitter(chunk_size=100, chunk_overlap=20)
            >>> text = "This is a long piece of text that needs to be split into smaller chunks."
            >>> chunks = splitter.split_text(text)
            >>> print(len(chunks))
            2
        """
        raise NotImplementedError  # pragma: no cover
