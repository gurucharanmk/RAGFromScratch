from pydantic import Field, BaseModel


class VectorDBConfig(BaseModel):
    """Base configuration for vector databases."""

    pass


class FAISSConfig(VectorDBConfig):
    """
    Configuration for FAISS vector database.

    Examples:
        >>> config = FAISSConfig(index_path="/path/to/faiss/index")
        >>> print(config.index_path)
        '/path/to/faiss/index'
    """

    index_path: str = Field(..., description="Path to the FAISS index")
