from search import search

TEST_CASES = [
    {
        "question": "How can Python be used for automation?",
        "expected_source": "automation.txt",
    },
    {
        "question": "How are databases used to store data?",
        "expected_source": "databases.txt",
    },
    {
        "question": "What is Javascript mainly used for?",
        "expected_source": "javascript.txt",
    },
     {
        "question": "How do computers communicate over networks?",
        "expected_source": "networking.txt",
    },
    {
        "question": "What is artificial intelligence?",
        "expected_source": "ai.txt",
    },
    {
        "question": "What are Python variables and data types?",
        "expected_source": "python.txt",
    },
    
]

def evaluate():
    correct = 0

    for case in TEST_CASES:
        question = case["question"]
        expected_source = case["expected_source"]

        results = search(question, top_k=3)

        retrieved_sources = [
            result["filename"]
            for result in results
        ]

        hit = expected_source in retrieved_sources

        if hit:
            correct += 1

        print("\nQuestion:", question)
        print("Expected:", expected_source)
        print("Retrieved:", retrieved_sources)
        print("PASS" if hit else "FAIL")

    accuracy = correct / len(TEST_CASES)

    print("\n====================")
    print("RETRIEVAL EVALUATION")
    print("\n====================")
    print(f"Correct: {correct}/{len(TEST_CASES)}")
    print(f"Hit@3: {accuracy:.2%}")


if __name__ == "__main__":
    evaluate()