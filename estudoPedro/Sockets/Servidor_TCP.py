from socket import *

servidor="127.0.0.1" #localhost
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM) #AF_INET: Tipo de identificação utilizando o IP; SOCK_STREAM: para trabalhar com o TCP
obj_socket.bind((servidor,porta)) # Seta o Servidor com o endereço
obj_socket.listen(2) # Quantos clientes terão acesso

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente!'
        con.send(msg_enviada)
        break
    con.close()