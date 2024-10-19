from unittest.mock import patch
from src.models.ollama_model import OllamaModel


def test_ollama_model_init(mock_ollama_config):
    model = OllamaModel(mock_ollama_config)
    assert model.model_name == "llama2"


@patch("ollama.generate")
def test_ollama_model_generate(mock_generate, mock_ollama_config):
    mock_generate.return_value = {"response": "Test response"}
    model = OllamaModel(mock_ollama_config)
    response = model.generate("Test prompt")
    assert response == "Test response"
    mock_generate.assert_called_once_with(model="llama2", prompt="Test prompt")


@patch("ollama.embeddings")
def test_ollama_model_embeddings(mock_embeddings, mock_ollama_config):
    mock_embeddings.return_value = {"embedding": [0.1, 0.2, 0.3]}
    model = OllamaModel(mock_ollama_config)
    embeddings = model.get_embeddings("Test text")
    assert embeddings == [0.1, 0.2, 0.3]
    mock_embeddings.assert_called_once_with(model="llama2", prompt="Test text")
