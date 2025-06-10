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

# Zone de texte + reconnaissance vocale JS
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

# Champ texte avec bouton vocal
st.text_input("Pose ta question :", key="user_input", label_visibility="collapsed")

col1, col2 = st.columns([4, 1])
with col1:
    st.button("Envoyer", key="submit_button")
with col2:
    st.markdown('<button onclick="startRecognition()">🎙 Parler</button>', unsafe_allow_html=True)

# Traitement de la réponse
user_input = st.session_state.get("user_input", "").strip()
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.chat_history.append(("bot", response))
    

    st.experimental_rerun()

