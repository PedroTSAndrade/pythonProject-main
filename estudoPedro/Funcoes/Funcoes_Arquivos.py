def chamarMenu():
    return int(input("Digite: "
        "\n<1> para registrar ativo"
        "\n<2> para gerar arquivo"
        "\n<3> para exibir ativos armazenados"
        "\n<4> para limpar o arquivo"
        "\n<5> para SAIR: "))

def registrar(inventario):
    resp="S"
    while resp=="S":
        inventario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        print("Registrado com sucesso!")
        resp=input("Digite <S> para continuar.").upper()

def persistir(inventario):
    basedados=[]
    lista=[]
    with open("inventario.csv","r") as arquivo:
        for registro in arquivo.readlines():
            basedados.append(registro.split(";"))
    if basedados[0][0] == "Plaqueta":
        print("tudo certo")
    elif basedados[0][0] != "Plaqueta":
        print("não é plaqueta: " + basedados[0][0])
    for chave,linha in inventario.items():
        lista=[str(chave), str(linha[0]),str(linha[1]),str(linha[2])]

    print(lista)
    print(basedados)
    basedados.append(lista)
    print(basedados)

#   PARTE QUE ESTÁ FUNCIONANDO CORRETAMENTE
#    with open("inventario.csv", "a") as inv:
#        #inv.write("Plaqueta;Data;Descrição;Departamento\n")
#        for chave, valor in inventario.items():
#            inv.write(chave + ";" + valor[0] + ";" +
#					valor[1] + ";" +valor[2]+"\n")
#    return print("Arquivo gerado com sucesso!")

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas=inv.readlines()
        for linha in linhas:
            lista = linha.split(";")
            print("Plaqueta.....: ", lista[0])
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
#    return print(str(linhas))

def limpar():
    with open("inventario.csv", "w") as inv:
        inv.write("")
    return print("Arquivo limpo!")