from rapidfuzz import fuzz
from src.preprocess import clean


def get_best_match(user_input, faq_list):
    """
    Matching V1:
    - Clean user input
    - Compare with every FAQ question
    - Use token_set_ratio
    - Return best matching answer
    """

    user_input = clean(user_input)

    best_score = 0
    best_answer = None
    best_question = None

    for faq in faq_list:
        question = clean(faq["question"])

        score = fuzz.token_set_ratio(user_input, question)

        if score > best_score:
            best_score = score
            best_answer = faq["answer"]
            best_question = faq["question"]

    return {
        "answer": best_answer,
        "score": best_score,
        "matched_question": best_question
    }