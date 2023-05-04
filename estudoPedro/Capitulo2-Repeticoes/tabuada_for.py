numero=int(input("Digite um número para a tabuada: "))

for multiplo in range(1,11,1):
    print(str(numero) + " * " + str(multiplo) + " = " + str((numero*multiplo)))