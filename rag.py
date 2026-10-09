from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 3,
        "score_threshold": 0.5
    }
)


def retrieve_context(question):

    documents = retriever.invoke(question)

    if not documents:
        return None

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context