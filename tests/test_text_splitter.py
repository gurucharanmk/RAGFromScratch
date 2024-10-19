from src.text_splitter.recursive_splitter import RecursiveTextSplitter


def test_recursive_splitter_init():
    splitter = RecursiveTextSplitter(chunk_size=100, chunk_overlap=20)
    assert splitter.chunk_size == 100
    assert splitter.chunk_overlap == 20


def test_recursive_splitter_split():
    splitter = RecursiveTextSplitter(chunk_size=10, chunk_overlap=2)
    text = "This is a test text for splitting."
    chunks = splitter.split_text(text)
    assert len(chunks) > 0
    assert all(len(chunk) <= 10 for chunk in chunks)
