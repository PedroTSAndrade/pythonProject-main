ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "), input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo ip´s: ")
for ip, nome in ips.items():
    print(ip[0] + "." + ip[1] + " - " + nome)

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa=input("Digite os dois últimos octetos: ")
print("Máquinas no mesmo endereço (redes diferentes):")
for ip,nome in ips.items():
    if(ip[1]==pesquisa):
        #print(nome)
        print(ip[0] + "." + ip[1] + " - " + nome)

print("Exibindo máquinas que compõem a mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
print("Máquinas na mesma rede:")
for ip,nome in ips.items():
    if(ip[0]==rede):
        #print(nome)
        print(ip[0] + "." + ip[1] + " - " + nome)