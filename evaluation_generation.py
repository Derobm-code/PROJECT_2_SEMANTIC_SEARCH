from evaluator import evaluate_answer
from generator import generate_answer
from search import search


TEST_CASES = [
    {
        "question": "How can Python be used for automation?",
        "must_cover": [
            "repetitive tasks",
            "files and directories",
            "CSV and JSON",
        ],
    },
    {
        "question": "How are databases used to store data?",
        "must_cover": [
            "store and organize data",
            "relational databases",
            "tables and SQL",
            "NoSQL",
        ],
    },
    {
        "question": "What is JavaScript mainly used for?",
        "must_cover": [
            "web interactivity",
            "browsers",
            "Node.js",
        ],
    },
]

def build_context(results: list[dict]) -> str:
    context_parts = []

    for i, result in enumerate(results, start=1):
        context_parts.append(
            f"[Source] {i}: "
            f"{result['filename']} "
            f"chunk {result['chunk_number']}]\n"
            f"{result['text']}"
        )

    return "\n\n".join(context_parts)

def main():
    passed_tests = 0

    for case in TEST_CASES:
        question = case["question"]

        print("\n" + "=" * 60)
        print(f"QUESTION: {question}")
        print("=" * 60)

        results = search(question, top_k=3)

        if not results:
            print("\nNo relevant information found.")
            print("RESULT: FAIL")
            continue

        context = build_context(results)

        answer = generate_answer(
            question=question,
            context=context,
        )

        evaluation = evaluate_answer(
            question=question,
            context=context,
            answer=answer,
            must_cover=case["must_cover"],
        )

        print("\nANSWER")
        print(answer)

        print("\nEVALUATION:")
        print(
            f"\nAnswers question: "
            f"{evaluation.answers_question}"
        )

        for fact in evaluation.facts:
            print(f"\nFact: {fact.fact}")
            print(f"Covered: {fact.covered}")
            print(
                f"Supported by context: "
                f"{fact.supported_by_context}"
            )

        print(
            "\nUnsupported claims:",
            evaluation.unsupported_claims,
        )

        print(
            "\nRESULT:",
            "PASS" if evaluation.passed else "FAIL"
        )

        if evaluation.passed:
            passed_tests += 1

    print("\n" + "=" * 60)
    print("GENERATION EVALUATION")
    print("=" * 60)

    print(
        f"Passed: {passed_tests}/{len(TEST_CASES)}"
    )

if __name__ == "__main__":
    main()
