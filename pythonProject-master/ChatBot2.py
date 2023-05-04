from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("BotPeo")

# isso aqui só será utilizado para corrigir o bug
from spacy.cli import download

download("en_core_web_sm")
class ENGSM:
	ISO_639_1 = 'en_core_web_sm'
    
chatbot = ChatBot("BotPeo", tagger_language=ENGSM)
