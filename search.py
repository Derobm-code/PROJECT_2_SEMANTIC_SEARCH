from embeddings import get_embedding
#from similarity import cosine_similarity
from vector_store import collection

MIN_SIMILARITY = 0.30


def search(
    query: str,
    #index: list[dict],
    top_k: int = 3
):
    query_embedding = get_embedding(query)

    raw_results = collection.query(
        query_embeddings=[query_embedding], 
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    results = []

    for i in range(len(raw_results["ids"][0])):
        distance = raw_results["distances"][0][i]
        similarity = 1 - distance

        if similarity < MIN_SIMILARITY:
            continue
        metadata = raw_results["metadatas"][0][i]

        results.append({
            "filename": metadata["filename"],
            "chunk_number": metadata["chunk_number"],
            "text": raw_results["documents"][0][i],
            "similarity": similarity,

        })

    return results



    












# def search(query: str, documents: dict[str, str], top_k: int = 3):
#     query_embedding = get_embedding(query)

#     results = []

#     for filename, text in documents.items():
#         document_embedding = get_embedding(text)

#         score = cosine_similarity(
#             query_embedding,
#             document_embedding
#         )

#         results.append((filename, score, text))

#     results.sort(key=lambda x: x[1], reverse=True)

#     return results[:top_k]