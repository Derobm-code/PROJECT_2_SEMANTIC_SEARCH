from ollama import chat

from evaluation_models import GenerationEvaluation

def evaluate_answer(
    question: str,
    context: str,
    answer: str,
    must_cover: list[str],
) -> GenerationEvaluation:

    facts = "\n".join(
        f"- {fact}"
        for fact in must_cover
    )

    prompt = f"""
You are evaluating an answer produced by a RAG system.

Evaluate three things:

1. Does the answer actually answer the user's question?
2. Does the answer cover every required fact?
3. Are the factual claims supported by the provided context?

Question:
{question}

CONTEXT:
{context}

ANSWER:
{answer}

REQUIRED FACTS:
{facts}

Rules:

- answers_question = true only when the answer directly addresses
  the user's question.
- covered = true only when the answer clearly communicates the fact.
- supported_by_context = true only when the context supports the fact.
- Add factual claims to unsupported_claims if they are not supported
  by the provided context.
- Do not treat a fact as relevant merely because it appears somewhere
  in the context.
- passed = true only if:
    1. answers_question is true
    2. every required fact is covered
    3. every required fact is supported by the context
    4. unsupported_claims is empty
"""

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format=GenerationEvaluation.model_json_schema(),
        options={"temperature": 0},
    )

    return GenerationEvaluation.model_validate_json(
        response.message.content
    )