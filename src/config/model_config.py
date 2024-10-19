from pydantic import Field, BaseModel


class ModelConfig(BaseModel):
    """Base configuration for language models."""

    pass


class OllamaConfig(ModelConfig):
    """
    Configuration for Ollama models.

    Examples:
        >>> config = OllamaConfig(model_name="llama2")
        >>> print(config.model_name)
        'llama2'
    """

    llm_model: str = Field(..., description="Name of the Ollama model")
