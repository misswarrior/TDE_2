import random
vetor = [random.randint(0, 20) for valores in range(50)]
print(vetor)

#soma
somaVetor = sum(vetor)
print("A soma do vetor é: " + str(somaVetor))

#ocorrencias do numero 9
import collections
repetido = collections.Counter(vetor)
print("O número 9 repetiu " + str(repetido[9]) + " vezes.")

#maior valor no vetor
maior = max(vetor)
print("O maior valor no vetor é " + str(maior))

#menor numero no vetor
menor = min(vetor)
print("o menor valor no vetor é " + str(menor))