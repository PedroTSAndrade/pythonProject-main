# pyAudio = Lê o áudio do microfone
# Speech Recognition = Reconhece a voz com microfone

import speech_recognition as sr

def ouvir_microfone():

    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Fale alguma coisa...')
        #armazena o que o usuário falou em uma variável
        audio = microfone.listen(source)

    #tenta fazer algo
    try:
        frase = microfone.recognize_google(audio, language="pt-BR")
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print('Não consegui compreender o que você disse!')
    return frase

while True:
    ouvir_microfone()
    continuar = str(input("Deseja Continuar? S/N")).upper()[0]

    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        print('Digite um comando válido.')