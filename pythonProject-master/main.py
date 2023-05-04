# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import pyttsx4
import datetime
import wikipedia
import pywhatkit

microfone = sr.Recognizer()
maquina = pyttsx4.init()

def ouvir_microfone():

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
            comandovoz = microfone.recognize_google(audio, language='pt-BR')
            comandovoz = comandovoz.lower()

            if 'teste' in comandovoz:
                comandovoz = comandovoz.replace('teste','')
                maquina.say(comandovoz)
                maquina.runAndWait()

    except:
        texto = 'O microfone não está funcionando!'
        print(texto)
        maquina.say(texto)
        maquina.runAndWait()
    return comandovoz

def comando_voz_usuario():
    saudacao = 'Olá, em que posso ajudar?'
    print(saudacao)
    maquina.say(saudacao)
    maquina.runAndWait()
    while True:
        comandovoz = ouvir_microfone()
        if 'desejo sair' in comandovoz:
            despedida = 'Foi um prazer conversar com você. Até à próxima'
            print(despedida)
            maquina.say(despedida)
            maquina.runAndWait()
            break
        elif 'que horas são agora' in comandovoz:
            hora = datetime.datetime.now().strftime('%H:%M')
            resultado = 'Agora são ' + hora
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
        elif 'procure por' in comandovoz:
            procurar = comandovoz.replace('procure por','')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,2)
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
        elif 'toque a música' in comandovoz:
            musica = comandovoz.replace('toque a música','')
            resultado = pywhatkit.playonyt(musica)
            texto = 'Tocando a música' + musica.title()
            print(texto)
            maquina.say(texto)
            maquina.runAndWait()
            break
        else:
            texto = 'Não consegui compreender o que disse!'
            print(texto)
            maquina.say(texto)
            maquina.runAndWait()

comando_voz_usuario()
