from Funcoes.Funcoes_Dicionario import *
usuarios={}

usuarios["1"]=["ptis".upper(),"adm".upper(),"Pedro".upper(),"08/06/2022","12:00","145001"]
usuarios["3"]=["favr".upper(),"adm".upper(),"Fabio".upper(),"08/06/2022","12:01","145002"]
usuarios["4"]=["algn".upper(),"adm".upper(),"Alessandro".upper(),"08/06/2022","11:00","145003"]
usuarios["2"]=["ghrb".upper(),"usr".upper(),"Gustavo".upper(),"08/06/2022","09:00","145004"]

opcao=perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":

        #SIMPLIFICADO
        #chave=input("Digite o login: ").upper()
        #usuarios[chave]=[input("Digite o nome: ").upper(),input("Digite a última data de acesso: ").upper(),input("Qual a última estação acessada: ").upper()]

        inserir(usuarios)

    elif opcao == "P":
        pesquisar(usuarios,input("Digite o código para pesquisa:").upper())

    elif opcao == "E":
        excluir(usuarios,input("Digite o código para exclusão:").upper())

    elif opcao == "L":
        listar(usuarios)

    opcao=perguntar()

print("Opção inválida")

