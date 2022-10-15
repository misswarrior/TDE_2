from typing import Set

vetor = []
valores = []
numerosRepetidos = set()
while True:
    valoresVetor = int(input("Digite um valor inteiro: "))
    vetor.append(valoresVetor)
    count = len(vetor)
    if count == 10:
        break
for numeros in vetor:
    if numeros not in valores:
        valores.append(numeros)
    else:
        numerosRepetidos.add(numeros)

print(numerosRepetidos)
