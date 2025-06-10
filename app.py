import streamlit as st
from chat import get_response, bot_name

st.set_page_config(page_title="Conseil-Bot", layout="centered")
st.title("🤖 Conseil-Bot - Service d'Urgence")

# Historique
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Affichage
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**👤 Vous :** {msg}")
    else:
        st.markdown(f"**🤖 {bot_name} :** {msg}")

# Zone de saisie
user_input = st.text_input("Pose ta question ici :", "")

# Bouton envoyer
if st.button("Envoyer") or user_input:
    if user_input.strip() != "":
        st.session_state.chat_history.append(("user", user_input))
        bot_reply = get_response(user_input)
        st.session_state.chat_history.append(("bot", bot_reply))
        st.experimental_rerun()
