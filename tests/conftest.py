import pytest
from unittest.mock import Mock
import numpy as np
from src.config.model_config import OllamaConfig
from src.config.vector_db_config import FAISSConfig
from src.config.data_source_config import PDFConfig
from src.models.ollama_model import OllamaModel
from src.vector_db.faiss_db import FAISSVectorDB
from src.data_source.pdf_source import PDFDataSource
from src.text_splitter.recursive_splitter import RecursiveTextSplitter


@pytest.fixture
def mock_ollama_config():
    return OllamaConfig(llm_model="llama2")


@pytest.fixture
def mock_faiss_config():
    return FAISSConfig(index_path="/tmp/test.index")


@pytest.fixture
def mock_pdf_config():
    return PDFConfig(pdf_path="/tmp/test.pdf")


@pytest.fixture
def mock_ollama_model(mock_ollama_config):
    model = Mock(spec=OllamaModel)
    model.model_name = mock_ollama_config.llm_model
    model.generate.return_value = "Test response"
    model.get_embeddings.return_value = np.random.rand(384).tolist()
    return model


@pytest.fixture
def mock_faiss_db(mock_faiss_config):
    db = Mock(spec=FAISSVectorDB)
    db.file_path = mock_faiss_config.index_path
    db.add_embeddings.return_value = None
    db.search.return_value = [
        {"distance": 0.1, "index": 0, "text": "Test document 1"},
        {"distance": 0.2, "index": 1, "text": "Test document 2"},
    ]
    return db


@pytest.fixture
def mock_pdf_source(mock_pdf_config):
    source = Mock(spec=PDFDataSource)
    source.pdf_path = mock_pdf_config.pdf_path
    source.load_data.return_value = ["Test document 1", "Test document 2"]
    return source


@pytest.fixture
def text_splitter():
    return RecursiveTextSplitter(chunk_size=10, chunk_overlap=2)
