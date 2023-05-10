from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

#download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

# Cria um novo chat, nomeado
chatbot = ChatBot("BotPeo", tagger_language=ENGSM)

trainer = ListTrainer(chatbot)

trainer.train([
    "Olá, como posso ajudar?",
    "Claro, gostaria de reservar um voo para Guarulhos.",
    "Seu voo foi reservado."
])

# Obtenha uma resposta para o texto de entrada. Gostaria de reservar um voo'
resposta = chatbot.get_response('Gostaria de reservar um voo.')

print(resposta)