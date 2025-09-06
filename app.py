import streamlit as st
import streamlit.components.v1 as components
import json

# Load responses
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

# Page config
st.set_page_config(page_title="WhisperBot", layout="centered")

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>WhisperBot</h1>", unsafe_allow_html=True)

# Input
user_input = st.text_input("You:", "")

# Response
if user_input:
    reply = responses.get(user_input.lower(), "I hear you. Quietly.")
    st.markdown(f"<div class='bot-reply'>{reply}</div>", unsafe_allow_html=True)
