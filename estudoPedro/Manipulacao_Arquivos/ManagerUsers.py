from Funcoes.Funcoes_Dicionario import *
usuarios={}
opcao=perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserirUsuario(usuarios)
    elif opcao=="P":
        pesquisarUsuario()
    elif opcao=="E":
        excluirUsuario()
    elif opcao=="L":
        print("faz nada por enquanto")
    opcao = perguntar()