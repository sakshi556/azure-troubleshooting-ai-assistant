from pathlib import Path

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


file_path = Path("knowledge/azure_functions.txt")

text = file_path.read_text(encoding="utf-8")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

documents = text_splitter.create_documents(
    [text],
    metadatas=[{"source": str(file_path)}]
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = FAISS.from_documents(
    documents,
    embeddings
)

vector_store.save_local("faiss_index")

print("FAISS knowledge index created successfully.")