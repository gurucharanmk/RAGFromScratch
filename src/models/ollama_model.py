from typing import List
import ollama
from .base import LanguageModel
from ..config.model_config import OllamaConfig


class OllamaModel(LanguageModel):
    """
    Ollama implementation of LanguageModel.

    This class provides methods to generate text and embeddings using Ollama models.

    Examples:
        >>> from ..config.model_config import OllamaConfig
        >>> config = OllamaConfig(llm_model="llama2")
        >>> model = OllamaModel(config)
        >>> response = model.generate("Your question here")
        >>> print(response)
        'LLM response here.'
    """

    def __init__(self, config: OllamaConfig) -> None:
        """
        Initialize Ollama model for generation and embedding.

        Args:
            config (OllamaConfig): Configuration object for the Ollama model.

        Examples:
            >>> from ..config.model_config import OllamaConfig
            >>> config = OllamaConfig(llm_model="llama3.2")
            >>> model = OllamaModel(config)
        """
        self.model_name: str = config.llm_model

    def generate(self, prompt: str) -> str:
        """
        Generate text using Ollama model.

        Args:
            prompt (str): The input prompt for text generation.

        Returns:
            str: The generated text response.

        Examples:
            >>> model = OllamaModel(OllamaConfig(llm_model="llama2"))
            >>> response = model.generate("Who is father of AI.")
            >>> print(response)
            'The title "father of AI" is often attributed to John McCarthy, an American computer scientist who coined the term "artificial intelligence" in 1956....'
        """
        response: dict[str, str] = ollama.generate(model=self.model_name, prompt=prompt)
        return response["response"]

    def get_embeddings(self, text: str) -> List[float]:
        """
        Get embeddings using Ollama model.

        Args:
            text (str): The input text to generate embeddings for.

        Returns:
            List[float]: A list of floating-point numbers representing the embedding.

        Examples:
            >>> model = OllamaModel(OllamaConfig(llm_model="llama2"))
            >>> embeddings = model.get_embeddings("Hello, world!")
            >>> print(len(embeddings))
            4096  # The actual number may vary depending on the model
            >>> print(embeddings[:5])
            [0.023, -0.041, 0.017, 0.089, -0.032]  # Example values
        """
        response: dict[str, List[float]] = ollama.embeddings(
            model=self.model_name, prompt=text
        )
        return response["embedding"]
