vetor = []
while True:
    valoresVetor = int(input("Digite um valor inteiro: "))
    if valoresVetor < 0:
        break
    else:
        vetor.append(valoresVetor)
print("O vetor é " + str(vetor))

#numeros maiores que 5
maiores = 0
for numero in vetor:
    if numero > 5:
        maiores += 1
print("numeros maiores que 5: " +str(maiores))

#soma pares
somaPares = 0
for numero in vetor:
    if numero%2 == 0:
       somaPares += numero
print("Soma dos pares :" + str(somaPares))

#soma impares
somaImpares = 0
for numero in vetor:
    if numero%2 !=0:
        somaImpares += numero
print("Soma dos ímpares: " + str(somaImpares))

#Quantidade de valores no vetor
print("Foram armazenados " + str(len(vetor)) + " valores no vetor.")
