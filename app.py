import re
import streamlit as st
from src.data_loader import load_faqs
from src.matcher import get_best_match

faqs = load_faqs()

st.title("FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def is_gibberish(text):
    letters = re.findall(r"[a-zA-Z]", text)
    return len(letters) / max(len(text), 1) < 0.4

user_input = st.text_input("Ask your question:")

if st.button("Submit"):

    if not user_input.strip():
        st.warning("Please enter a valid question.")

    elif len(user_input) > 150:
        st.warning("Question too long. Please shorten it.")

    elif is_gibberish(user_input):
        st.warning("Please enter a meaningful question.")

    else:
        result = get_best_match(user_input, faqs)

        if result["score"] < 50:
            answer = "Sorry, I couldn't find a good match."
        else:
            answer = result["answer"]


        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(("Bot", answer))

for role, msg in st.session_state["messages"]:
    st.write(f"**{role}:** {msg}")