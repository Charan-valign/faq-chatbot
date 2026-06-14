import re
import os
import streamlit as st
from src.data_loader import load_faqs
from src.matcher import get_best_match

faqs = load_faqs()

st.title("FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Log unanswered questions
def log_unanswered(question, score):
    os.makedirs("logs", exist_ok=True)
    with open("logs/unanswered.txt", "a", encoding="utf-8") as f:
        f.write(f"{question} | score: {score}\n")


# Gibberish detection
def is_gibberish(text):
    text = text.strip()
    letters = re.findall(r"[a-zA-Z]", text)
    return len(letters) / max(len(text), 1) < 0.4

# Input
user_input = st.text_input("Ask your question:")

if st.button("Submit"):

    # 1. Empty input check
    if not user_input.strip():
        st.warning("Please enter a valid question.")

    # 2. Length check
    elif len(user_input) > 150:
        st.warning("Question too long. Please shorten it.")

    # 3. Gibberish check
    elif is_gibberish(user_input):
        st.warning("Please enter a meaningful question.")

    else:
        # 4. Get match
        result = get_best_match(user_input, faqs)

        # 5. Decide answer
        if result["score"] < 50:
            answer = "Sorry, I couldn't find a good match."
            log_unanswered(user_input, result["score"])
        else:
            answer = result["answer"]

        # 6. Store chat
        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(
            ("Bot", f"{answer} (Confidence: {result['score']:.2f}%)")
        )

# Display chat history
for role, msg in st.session_state["messages"]:
    st.write(f"**{role}:** {msg}")