from src.rag_system import RAGSystem
from src.text_splitter.recursive_splitter import RecursiveTextSplitter


def test_rag_system_init(
    mock_ollama_config,
    mock_faiss_config,
    mock_pdf_config,
    mock_ollama_model,
    mock_faiss_db,
    mock_pdf_source,
):
    rag = RAGSystem(mock_ollama_config, mock_faiss_config, mock_pdf_config)
    assert isinstance(rag.text_splitter, RecursiveTextSplitter)


def test_rag_system_index_data(
    mock_ollama_config,
    mock_faiss_config,
    mock_pdf_config,
    mock_ollama_model,
    mock_faiss_db,
    mock_pdf_source,
):
    rag = RAGSystem(mock_ollama_config, mock_faiss_config, mock_pdf_config)
    rag.model = mock_ollama_model
    rag.vector_db = mock_faiss_db
    rag.data_source = mock_pdf_source

    rag.index_data()

    mock_pdf_source.load_data.assert_called_once()
    assert mock_ollama_model.get_embeddings.call_count > 0
    mock_faiss_db.add_embeddings.assert_called_once()


def test_rag_system_query(
    mock_ollama_config,
    mock_faiss_config,
    mock_pdf_config,
    mock_ollama_model,
    mock_faiss_db,
    mock_pdf_source,
):
    rag = RAGSystem(mock_ollama_config, mock_faiss_config, mock_pdf_config)
    rag.model = mock_ollama_model
    rag.vector_db = mock_faiss_db
    rag.data_source = mock_pdf_source

    response = rag.query("Test question")

    mock_ollama_model.get_embeddings.assert_called_once()
    mock_faiss_db.search.assert_called_once()
    mock_ollama_model.generate.assert_called_once()
    assert isinstance(response, str)
