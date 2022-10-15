vetor = []
listaRep = []
count = 0
while True:
    valoresVetor = int(input("Digite um valor inteiro: "))
    vetor.append(valoresVetor)
    count = len(vetor)
    if count == 20:
        break
    for valor in vetor:
        if valor not in listaRep:
            listaRep.append(valor)

print(vetor)
print("O vetor sem repetição é: " + str(listaRep))
