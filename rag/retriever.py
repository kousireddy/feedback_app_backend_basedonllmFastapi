from .vector_store import VectorStore
from .embedder import embeddings

store = VectorStore()

def add_feedback(feedback_list):
    embs = embeddings.embed_documents(feedback_list)
    store.add(embs, feedback_list)

def retrieve(query):
    q_emb = embeddings.embed_query(query)
    return store.search(q_emb)