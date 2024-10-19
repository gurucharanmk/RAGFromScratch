from typing import List
from .base import DataSource
from ..config.data_source_config import PDFConfig
import PyPDF2


class PDFDataSource(DataSource):
    """
    PDF implementation of DataSource.

    This class provides methods to load data from PDF files.

    Examples:
        >>> from ..config.data_source_config import PDFConfig
        >>> config = PDFConfig(pdf_path="/path/to/document.pdf")
        >>> pdf_source = PDFDataSource(config)
        >>> documents = pdf_source.load_data()
        >>> print(len(documents))
        5
    """

    def __init__(self, config: PDFConfig) -> None:
        """
        Initialize PDF data source.

        Args:
            config (PDFConfig): Configuration object for the PDF data source.

        Examples:
            >>> from ..config.data_source_config import PDFConfig
            >>> config = PDFConfig(pdf_path="/path/to/document.pdf")
            >>> pdf_source = PDFDataSource(config)
        """
        self.pdf_path: str = config.pdf_path

    def load_data(self) -> List[str]:
        """
        Load data from PDF file.

        Returns:
            List[str]: A list of strings, where each string represents the text content of a page.

        Examples:
            >>> pdf_source = PDFDataSource(PDFConfig(pdf_path="/path/to/document.pdf"))
            >>> documents = pdf_source.load_data()
            >>> print(len(documents))
            5
            >>> print(documents[0][:50])
            'This is the content of the first page of the PDF...'
        """
        with open(self.pdf_path, "rb") as file:
            reader: PyPDF2.PdfReader = PyPDF2.PdfReader(file)
            return [page.extract_text() for page in reader.pages]
