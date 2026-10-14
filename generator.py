from ollama import chat

def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a helpful assistant answering questions from a knowledge base.

Answer the user's question using ONLY the provided context.

Important rules:
- Do not use outside knowledge.
- If the context does not contain enough information, say so.
- Cite the source number after each factual claim.
- Use citations in the format [1], [2], [3].
- Only cite sources that actually support the claim.
- Do not invent source numbers.


Context:
{context}

Question:
{question}
"""

    response = chat(
        model="qwen3:1.7b", 
        messages=[
            {"role": "user", 
            "content": prompt,}],)

    return response.message.content