import streamlit as st
from src.data_loader import load_faqs
from src.matcher import get_best_match

faqs = load_faqs()

st.title("FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("Ask your question:")

if user_input:
    result = get_best_match(user_input, faqs)

    if result["score"] < 50:
        answer = "Sorry, I couldn't find a good match."
    else:
        answer = result["answer"]

    st.session_state["messages"].append(("You", user_input))
    st.session_state["messages"].append(("Bot", answer))

for role, msg in st.session_state["messages"]:
    st.write(f"**{role}:** {msg}")

if user_input:
    if not user_input.strip():
        st.warning("Please enter a valid question.")
    elif len(user_input) > 150:
        st.warning("Question too long. Please shorten it.")