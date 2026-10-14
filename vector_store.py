import chromadb


client =  chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base",
    metadata={"hnsw:space": "cosine"},
)

def add_chunks(chunks: list[dict]) -> None:
    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for chunk in chunks:
        ids.append(chunk["id"])
        documents.append(chunk["text"])
        embeddings.append(chunk["embedding"])
        metadatas.append({
            "filename": chunk["filename"],
            "chunk_number": chunk["chunk_number"],
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )