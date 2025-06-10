import streamlit as st
from chat import get_response, bot_name

st.set_page_config(page_title="Conseil-Bot", layout="centered")
st.title("🤖 Conseil-Bot - Service d'Urgence")

# Historique de conversation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Affiche les messages précédents
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**👤 Vous :** {msg}")
    else:
        st.markdown(f"**🤖 {bot_name} :** {msg}")

# Champ texte (sans reconnaissance vocale)
st.text_input("Pose ta question :", key="user_input", label_visibility="collapsed")

# Bouton unique
if st.button("Envoyer", key="submit_button"):
    user_input = st.session_state.get("user_input", "").strip()
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = get_response(user_input)
        st.session_state.chat_history.append(("bot", response))

