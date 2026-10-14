from evaluator import evaluate_answer
from search import search

QUESTION = "How are databases used to store data?"

MUST_COVER = [
    "store and organize data",
    "relational databases",
    "tables and SQL",
    "NoSQL",
]

BAD_ANSWER = """
All databases use SQL tables to store data.
There is no meaningful difference between relational 
databases and NoSQL databases, because NoSQL databases 
also require SQL tables.
"""

def build_context(results: list[dict]) -> str:
    context_parts = []

    for i, result in enumerate(results, start=1):
        context_parts.append(
            f"[Source] {i}: "
            f"{result['filename']}, "
            f"chunk {result['chunk_number']}]\n"
            f"{result['text']}"
        )

    return "\n\n".join(context_parts)

def main():
    results = search(QUESTION, top_k=3)

    if not results:
        print("No relevant context found.")
        return

    context = build_context(results)

    evaluation = evaluate_answer(
        question=QUESTION,
        context=context,
        answer=BAD_ANSWER,
        must_cover=MUST_COVER,
    )

    print("\nBAD_ANSWER:")
    print(BAD_ANSWER)

    print("\nEVALUATION")
    print(f"Answers question: {evaluation.answers_question}")

    for fact in evaluation.facts:
        print(f"\nFact: {fact.fact}")
        print(f"Covered: {fact.covered}")
        print(
            f"Supported by context: "
            f"{fact.supported_by_context}"
        )
    print(
        "\nFINAL RESULT:",
        "PASS" if evaluation.passed else "FAIL"
    )


if __name__ == "__main__":
    main()