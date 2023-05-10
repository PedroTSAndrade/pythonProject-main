from chatterbot import ChatBot

# Descomente as seguintes linhas para habilitar o log detalhado
import logging
logging.basicConfig(level=logging.INFO)

# Crie uma nova instância de um ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

print('Digite algo para começar...')

# O loop a seguir será executado sempre que o usuário inserir a entrada
while True:
    try:
        user_input = input()

        bot_resposta = bot.get_response(user_input)

        print(bot_resposta)

    # Pressione ctrl-c ou ctrl-d no teclado para sair
    except (KeyboardInterrupt, EOFError, SystemExit):
        break