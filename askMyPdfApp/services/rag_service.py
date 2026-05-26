from .keyword_service import keyword_search


def ask_question(question):
    from .llm_service import generate_answer

    context_chunks = keyword_search(question)
    context = "\n".join(context_chunks)

    return generate_answer(context, question)