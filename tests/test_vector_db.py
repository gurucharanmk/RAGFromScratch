from unittest.mock import patch, Mock
from src.vector_db.faiss_db import FAISSVectorDB


def test_faiss_db_init(mock_faiss_config):
    db = FAISSVectorDB(mock_faiss_config)
    assert db.file_path == "/tmp/test.index"
    assert db.index is None
    assert db.dimension is None
    assert db.texts == []


@patch("faiss.IndexFlatL2")
@patch("faiss.write_index")
def test_faiss_db_add_embeddings(mock_write_index, mock_index_class, mock_faiss_config):
    mock_index = Mock()
    mock_index_class.return_value = mock_index

    db = FAISSVectorDB(mock_faiss_config)
    embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    metadata = [{"text": "doc1"}, {"text": "doc2"}]

    db.add_embeddings(embeddings, metadata)

    assert db.dimension == 3
    assert db.texts == ["doc1", "doc2"]
    mock_index.add.assert_called_once()
    mock_write_index.assert_called_once_with(mock_index, "/tmp/test.index")
