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
        print(f'{num} * {n} = {num * n}')
# tabuada()

# 50. somar 6 numeros apenas se forem pares
def somarPares():
    soma = 0
    for n in range(0, 6):
        num = int(input('Digite um nº: '))
        if num % 2 == 0:
            soma += num
            print(f'Soma parcial: {soma}')
    print(soma)
# somarPares()

# 51. 1º termo e razão de uma PA. Assistir à aula
def pa():
    r = 2
    for n in range(0, 11, r):
        print(n)
# pa()

# 52. ler um inteiro e dizer se ele é primo
def nPrimo():
    num = int(input('DIgite um nº: '))
    # if num % num == 0 and num % 1 == 0:
    #     print('É primo')
    # else:
    #     print('n é primo')
# nPrimo()

# 53. Assistir à aula
def palidromo():
    frase = str(input('Digite uma frase: '))
    frase = frase.replace(" ", "").lower()

    if frase == frase[::-1]:
        print('é um palíndromo')
    else:
        print('não é um palíndromo')
# palidromo()

# 54. atingiu maioridade
def maioridade():
    maiores = 0
    menores = 0
    anoAtual = datetime.date.today().year
    for idades in range(0, 7):
        idade = int(input('Em que ano vc nasceu? (digite no formato AAAA)'))
        if anoAtual - idade < 18:
            menores += 1
        elif anoAtual - idade > 18:
            maiores += 1
    print(f'Existem {maiores} maiores e {menores} menores')
# maioridade()

# 55. mostrar maior e menor peso
def mostrarPeso():
    maiorPeso = 0
    menorPeso = 0
    for p in range(0, 5):
        peso = float(input('Qual o seu peso? '))

        if peso >= maiorPeso:
            maiorPeso = peso

        if menorPeso == 0:
            menorPeso = peso
        elif peso <= menorPeso:
            menorPeso = peso

    print(f'O maior foi {maiorPeso} e o menor foi {menorPeso}')
# mostrarPeso()

# 56.