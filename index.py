from embeddings import get_embedding
from chunking import chunk_text


def create_chunks(documents: dict[str, str]) -> list[dict]:
    chunks = []

    for filename, text in documents.items():
        text_chunks = chunk_text(text, chunk_size=100, overlap=20,)

        for chunk_number, chunk in enumerate(text_chunks):
            chunks.append({
                "id": f"{filename}_{chunk_number}",
                "filename": filename,
                "chunk_number": chunk_number,
                "text": chunk,
                "embedding": get_embedding(chunk),
            })

    return chunks



   