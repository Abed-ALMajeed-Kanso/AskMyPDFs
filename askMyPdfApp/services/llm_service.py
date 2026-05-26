import os
from groq import Groq


def _get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Please define this environment variable.")
    return Groq(api_key=api_key)


def generate_answer(context, question):

    prompt = f"""
You are a helpful and precise assistant.

Rules:
- Use the provided context if it is relevant and sufficient.
- You may use general knowledge to answer the question if the context does not contain the answer.
- Always keep answers short (1–3 sentences maximum).
- Do not explain reasoning.

Answer behavior:
- If the answer is found in the context → answer based on the document and stay close to it.
- If the answer is NOT found in the context → answer using your general knowledge, but clearly add: "This is not found in the provided documents."

Special cases:
- If the user message is a greeting (e.g., "hello", "hi") or thanks (e.g., "thanks"), respond briefly and normally.

Context:
{context}

Question:
{question}

Answer:
"""

    client = _get_groq_client()
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content