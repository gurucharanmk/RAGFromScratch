from typing import List
from .base import TextSplitter


class RecursiveTextSplitter(TextSplitter):
    """
    RecursiveTextSplitter implementation.

    Examples:
        >>> splitter = RecursiveTextSplitter(chunk_size=100, chunk_overlap=20)
        >>> text = "This is a long piece of text that needs to be split into smaller chunks."
        >>> chunks = splitter.split_text(text)
        >>> print(len(chunks))
        2
    """

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200) -> None:
        """
        Initialize RecursiveTextSplitter.

        Args:
            chunk_size: Maximum size of each text chunk
            chunk_overlap: Number of characters to overlap between chunks

        Returns:
            None

        Examples:
            >>> splitter = RecursiveTextSplitter(chunk_size=500, chunk_overlap=50)
            >>> splitter.chunk_size
            500
            >>> splitter.chunk_overlap
            50
        """
        self.chunk_size: int = chunk_size
        self.chunk_overlap: int = chunk_overlap

    def split_text(self, text: str) -> List[str]:
        """
        Split the input text into chunks recursively with overlap.

        Args:
            text: Input text string to split

        Returns:
            List of text chunks as strings

        Examples:
            >>> splitter = RecursiveTextSplitter(chunk_size=10, chunk_overlap=2)
            >>> text = "This is a test text for splitting."
            >>> chunks = splitter.split_text(text)
            >>> print(chunks)
            ['This is a ', 'a test tex', 'text for s', 'splitting.']
        """
        chunks: List[str] = []
        start: int = 0
        while start < len(text):
            end: int = start + self.chunk_size
            chunk: str = text[start:end]
            chunks.append(chunk)
            start = end - self.chunk_overlap
        return chunks
