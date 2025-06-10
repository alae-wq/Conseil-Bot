import streamlit as st
from chat import get_response, bot_name
import uuid  # pour générer une clé unique

st.set_page_config(page_title="Conseil-Bot", layout="centered")
st.title("🤖 Conseil-Bot - Service d'Urgence")

# Historique de conversation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Affichage de l'historique
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**👤 Vous :** {msg}")
    else:
        st.markdown(f"**🤖 {bot_name} :** {msg}")

# Script JS pour reconnaissance vocale
st.markdown("""
    <script>
        function startRecognition() {
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = "fr-FR";
            recognition.onresult = function(event) {
                const text = event.results[0][0].transcript;
                document.getElementById("user_input").value = text;
                document.getElementById("submit_button").click();
            };
            recognition.start();
        }
    </script>
""", unsafe_allow_html=True)

# Champ texte avec clé unique (contourne le bug de session_state)
unique_input_key = str(uuid.uuid4())[:8]
user_input = st.text_input("Pose ta question :", key=unique_input_key, label_visibility="collapsed")

# Boutons
col1, col2 = st.columns([4, 1])
with col1:
    envoyer = st.button("Envoyer", key="submit_button")
with col2:
    st.markdown('<button onclick="startRecognition()">🎙 Parler</button>', unsafe_allow_html=True)

# Traitement de la réponse
if envoyer and user_input.strip():
    st.session_state.chat_history.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.chat_history.append(("bot", response))


    

