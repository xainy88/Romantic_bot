import streamlit as st
import sys
import os

# Add parent directory to Python path so we can import from logic/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.bot_core import get_bot_response

st.set_page_config(page_title="Minimalist Romantic Bot", layout="centered")
st.title("🖤 Minimalist Romantic Chatbot")

user_input = st.text_input("You:", "")

if user_input:
    response = get_bot_response(user_input)
    st.write("Bot:", response)