def perguntar():
    # pode ser direto no return: return input("O que deseja realizar...
    resposta = input("O que deseja realizar?" +
                  "\n<I> - Para Inserir um usuário" +
                  "\n<P> - Para Pesquisar um usuário" +
                  "\n<E> - Para Excluir um usuário" +
                  "\n<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Código: ").upper()]=[
        input("Digite o login: ").upper(),
        input("Nível de usuário: ").upper(),
        input("Digite o nome: ").upper(),
        input("Digite a última data de acesso: ").upper(),
        input("Digite a hora de acesso: ").upper(),
        input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, codigo):
    lista=dicionario.get(codigo)
    if lista != None:
            print("Login......: ", lista[0])
            print("Nível......: ", lista[1])
            print("Nome.......: ", lista[2])
            print("Data.......: ", lista[3])
            print("Hora.......: ", lista[4])
            print("Estação....: ", lista[5])

def excluir(dicionario, codigo):
    if dicionario.get(codigo) != None:
            del dicionario[codigo]
    print("Objeto excluído!")

def listar(dicionario):
    for codigo, valor in dicionario.items():
        print("Código...: ", codigo, " - Dados....: ", valor)


def inserirUsuario(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                input("Digite a última data de acesso: ").upper(),
                                                input("Qual a última estação acessada: ").upper()]
    salvarUsuario(dicionario)

def salvarUsuario(dicionario):
    with open("bd.txt","a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def pesquisarUsuario():
    with open("bd.txt","r") as arquivo:
        linhas=arquivo.readlines()
        for chave in linhas:
            print("Login: ", chave)

def excluirUsuario():
    with open("bd.txt","w") as arquivo:
        arquivo.write("")