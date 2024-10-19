from unittest.mock import mock_open, patch
from unittest.mock import Mock
from src.data_source.pdf_source import PDFDataSource


def test_pdf_source_init(mock_pdf_config):
    source = PDFDataSource(mock_pdf_config)
    assert source.pdf_path == "/tmp/test.pdf"


@patch("PyPDF2.PdfReader")
def test_pdf_source_load_data(mock_pdf_reader, mock_pdf_config):
    mock_page1 = Mock()
    mock_page1.extract_text.return_value = "Test content 1"
    mock_page2 = Mock()
    mock_page2.extract_text.return_value = "Test content 2"

    mock_pdf = Mock()
    mock_pdf.pages = [mock_page1, mock_page2]
    mock_pdf_reader.return_value = mock_pdf

    source = PDFDataSource(mock_pdf_config)

    with patch("builtins.open", mock_open()):
        documents = source.load_data()

    assert len(documents) == 2
    assert documents[0] == "Test content 1"
    assert documents[1] == "Test content 2"
