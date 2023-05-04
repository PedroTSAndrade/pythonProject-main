equipamentos=[]
valores=[]
seriais=[]
departamento=[]
resposta="N"
while resposta!="S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamento.append(input("Departamento: "))
  resposta=input("Digite \"S\" para sair: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento: " + str(indice+1))
  print("Nome: ", equipamentos[indice], " - Valor: ", valores[indice], " - Serial: ", seriais[indice], " - Departamento: ", departamento[indice])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
  if depreciacao==equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])

serial=int(input("Digite o número serial do equipamento que será descartado: "))
for indice in range(0,len(equipamentos)):
  if serial==seriais[indice]:
    del equipamentos[indice]
    del valores[indice]
    del seriais[indice]
    del departamento[indice]
    break

  for indice in range(0,len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Equipamento: ", equipamentos[indice], "Valor: ", valores[indice], "Serial: ", seriais[indice], "Departamento: ", departamento[indice])
