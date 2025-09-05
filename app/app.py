import streamlit as st
from chatbot_logic import get_response
import streamlit.components.v1 as components

# Falling hearts animation
falling_hearts_html = """
<style>
@keyframes fall {
  0% {transform: translateY(-100px);}
  100% {transform: translateY(100vh);}
}
.heart {
  position: fixed;
  top: -50px;
  font-size: 24px;
  color: pink;
  animation: fall 5s linear infinite;
}
</style>
<script>
function createHeart() {
  const heart = document.createElement("div");
  heart.className = "heart";
  heart.style.left = Math.random() * window.innerWidth + "px";
  heart.innerHTML = "💖";
  document.body.appendChild(heart);
  setTimeout(() => heart.remove(), 5000);
}
setInterval(createHeart, 500);
</script>
"""
components.html(falling_hearts_html, height=0)

# Chat UI
st.set_page_config(page_title="Romantic Bot", page_icon="💖", layout="centered")
st.markdown("<h1 style='text-align: center; color: pink;'>Emotionally Flat Romantic Chatbot</h1>", unsafe_allow_html=True)

user_input = st.text_input("Type your message here:")
if user_input:
    response = get_response(user_input)
    st.markdown(f"<div style='color: #ff69b4; font-size: 20px;'>{response}</div>", unsafe_allow_html=True)
