#   ELE TERIRA ESSA PARTE DURANTE O VÍDEO
#arquivo=open("primeiro_arquivo.txt","w")
#arquivo.write("Meu Primeiro Arquivo! ai que festa!")
#arquivo.close()

#   GRAVAÇÃO NO ARQUIVO DO TIPO APÊNDICE, MANTÉM O QUE TINHA E ADICIONA O NOVO
#with open("primeiro_arquivo.txt","a") as arquivo:
#    arquivo.write("\nSegunda linha de texto!")

#   ESTILO DE LEITURA DO ARQUIVO
#with open("primeiro_arquivo.txt","r") as arquivo:
#    conteudo=arquivo.read()
#    print("Tipo de dados da variável: ", type(conteudo))
#    print("Conteúdo do Arquivo:\n",conteudo)

#   EXEMPLO SEPARANDO O CONTEÚDO
with open("primeiro_arquivo.txt","r") as arquivo:
#   LÊ SOMENTE A PRIMEIRA LINHA DO ARQUIVO
#    conteudo=arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)