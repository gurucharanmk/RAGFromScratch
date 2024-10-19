from src.config.model_config import OllamaConfig
from src.config.vector_db_config import FAISSConfig
from src.config.data_source_config import PDFConfig


def test_ollama_config():
    config = OllamaConfig(llm_model="llama2")
    assert config.llm_model == "llama2"


def test_faiss_config():
    config = FAISSConfig(index_path="/tmp/test.index")
    assert config.index_path == "/tmp/test.index"


def test_pdf_config():
    config = PDFConfig(pdf_path="/tmp/test.pdf")
    assert config.pdf_path == "/tmp/test.pdf"
