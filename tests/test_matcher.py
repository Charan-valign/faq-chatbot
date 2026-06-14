import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.matcher import get_best_match
from src.data_loader import load_faqs

from src.matcher import get_best_match

faqs = [
    {
        "question": "How do I apply?",
        "answer": "Visit our website and fill the application form."
    },
    {
        "question": "What is the application fee?",
        "answer": "The application fee is Rs. 500."
    }
]

query = input("Ask a question: ")

result = get_best_match(query, faqs)

print("\nMatched Question:", result["matched_question"])
print("Score:", result["score"])
print("Answer:", result["answer"])  