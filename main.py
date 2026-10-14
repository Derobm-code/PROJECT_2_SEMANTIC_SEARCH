from pathlib import Path

from index import create_chunks
#from chunking import chunk_text
#from search import search

from vector_store import add_chunks

from generator import generate_answer

from search import search

def main():
    while True:
        query = input("Search: ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            print("Please enter a question.")
            continue

        results = search(query, top_k=3)

        if not results:
            print("\nNo relevant information was found " " in the knowledge base.")
            continue

        context_parts = []

        for i, result in enumerate(results, start=1):
            context_parts.append(
                f"[Source {i}: "
                f"{result['filename']}, "
                f"chunk {result['chunk_number']}]\n"
                f"{result['text']}"
            )

        context = "\n\n".join(context_parts)

        answer = generate_answer(
            question=query,
            context=context,
        )
        print("\nAnswer:")
        print(answer)

        for i, result in enumerate(results, start=1):
            print(
                f"[{i}] {result['filename']} "
                f"(chunk {result['chunk_number']} "
                f"-similarity: "
                f"{result['similarity']:.4f}"
            )
if __name__ == "__main__":
    main()

  