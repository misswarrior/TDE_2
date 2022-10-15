vetor = []
indice = 0

while True:
    valoresVetor = int(input("Digite um valor: "))
    vetor.append(valoresVetor)
    tamanhoVetor = len(vetor)
    if tamanhoVetor == 15:
        break

while indice < tamanhoVetor:
    while vetor[indice] == 0:
        vetor.pop(indice)
        tamanhoVetor = len(vetor)
    indice += 1

print(vetor)
