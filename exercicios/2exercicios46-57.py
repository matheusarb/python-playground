import datetime
import math
import os
import random
import calendar
import sys
import time

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 46. contagem regressiva fogos artifício de 10 a 0
def regressivaFogos():
    for r in range(10, 0, -1):
        print(r)
    print(0)
    print('Feliz ano novo!')
# regressivaFogos()

# 47. mostrar números pares
def numPares():
    for p in range(0, 51):
        if p % 2 == 0:
            print(p, end=" ")
# numPares()

# 48. soma números ímpares e múltiplos de 3
# bicho pegou aqui
def somaImpares():
    soma = 0

    for impar in range(1, 501):
        if impar % 2 != 0 and impar * 3 < 31:
            print(f'Resultado parcial da soma: {soma}')
            soma += impar

    print(soma)
# somaImpares()

# 49. taboada com o laço for
def tabuada():
    num = int(input('Digite um nº entre 1 e 10: '))
    for n in range(1, 11):
        print(f'{num} * {n} = {num*n}')
# tabuada()