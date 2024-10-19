from pydantic import BaseModel, Field


class DataSourceConfig(BaseModel):
    """Base configuration for data sources."""

    pass


class PDFConfig(DataSourceConfig):
    """
    Configuration for PDF data source.

    Examples:
        >>> config = PDFConfig(pdf_path="/path/to/document.pdf")
        >>> print(config.pdf_path)
        '/path/to/document.pdf'
    """

    pdf_path: str = Field(..., description="Path to the PDF file")
