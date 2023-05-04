import speech_recognition as sr #Biblioteca para rec. de voz (transcreve fala em texto)
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import comtypes.client as ct

tts = ct.CreateObject("sapi.SPVoice")
r = sr.Recognizer()

bot = ChatBot('Bot')
dialogo = ['Oi','Olá','olá','oi','tudo bem?','estou bem, e você?','estou bem','que bom'] #Lista de dialogos para treinar o bot
bot.set_trainer(ListTrainer)
bot.train(dialogo)
"""
def main():
  try:
    while True:
      with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # Ajustando ruído ambiente
        audio = r.listen(source) # Extrai áudio do microfone
        speech = r.recognize_google(audio, language='pt-BR') #transcrevendo fala em texto com api da Google
        print('Você: ', speech)
        response = bot.get_response(speech)
        print('Bot: ', response)
        resposta = (u""+str(response))
        tts.Speak(resposta)
  except sr.UnknownValueError:
        print('Erro de reconhecimento de fala')

if __name__ == "__main__":
    main()



"""