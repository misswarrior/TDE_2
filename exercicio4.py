vetor = []
while True:
    valoresVetor = int(input("Digite um numero inteiro: "))
    vetor.append(valoresVetor)
    count = len(vetor)
    if count == 6:
        break
print("Seu vetor é: " + str(vetor))

ordemInversa = list(reversed(vetor))
print("A ordem inversa é: " + str(ordemInversa))



