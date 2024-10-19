from src.config.model_config import OllamaConfig
from src.config.vector_db_config import FAISSConfig
from src.config.data_source_config import PDFConfig
from src.rag_system import RAGSystem


ollama_config = OllamaConfig(llm_model="llama3.2:1b")
faiss_config = FAISSConfig(index_path="./data/vector_strore/vdb.index")
pdf_config = PDFConfig(pdf_path="./data/source/press-physicsprize2024.pdf")

rag = RAGSystem(ollama_config, faiss_config, pdf_config)
rag.index_data()
response = rag.query("What is the prize amount ?")
print(response)
