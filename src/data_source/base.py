from abc import ABC, abstractmethod
from typing import List


class DataSource(ABC):
    """Abstract base class for data sources."""

    @abstractmethod
    def load_data(self) -> List[str]:
        """
        Load data from the source.

        Examples:
            >>> data_source = PDFDataSource(PDFConfig(pdf_path="/path/to/document.pdf"))
            >>> documents = data_source.load_data()
            >>> print(len(documents))
            5
        """
        raise NotImplementedError  # pragma: no cover
