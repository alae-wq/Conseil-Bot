import json
import random
import numpy as np
from sentence_transformers import SentenceTransformer

# Nom du bot
BOT_NAME = "Conseil-Bot"

# Chargement des intents
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Préparation des données
all_examples = []
all_tags = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        all_examples.append(pattern)
        all_tags.append(tag)

# Chargement du modèle
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
example_vectors = model.encode(all_examples)

# Fonction de similarité cosinus
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Prédiction de l'intention
def predict_intent(user_input, seuil=0.6):
    user_vec = model.encode([user_input])[0]
    similarities = [cosine_similarity(user_vec, vec) for vec in example_vectors]
    max_idx = np.argmax(similarities)
    max_sim = similarities[max_idx]
    if max_sim > seuil:
        return all_tags[max_idx]
    else:
        return None

# Génération de réponse
def generate_response(user_input):
    intent = predict_intent(user_input)
    if intent is None:
        return "Je n'ai pas compris, pouvez-vous reformuler ?"
    else:
        return random.choice(responses[intent])

# Fonction à utiliser dans app.py
def get_response(user_input):
    return generate_response(user_input)

# Variable à importer dans app.py
bot_name = BOT_NAME
