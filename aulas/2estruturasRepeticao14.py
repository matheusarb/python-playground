# Parte 2 de laços
# DO-WHILE
import time

num = 1
countPar = 0
countImpar = 0
while num != 0:
    num = int(input('Digite um nº: '))
    if num % 2 == 0:
        countPar += 1
    else:
        countImpar += 1
print(f'Foram digitados {countPar} nº\'s pares e {countImpar} nº\'s ímpares')
print('FIM')

