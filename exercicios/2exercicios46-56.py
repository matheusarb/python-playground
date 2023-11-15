import datetime
import math
import os
import random
import calendar
import sys
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 46. contagem regressiva fogos artifício de 10 a 0
def regressivaFogos():
    for r in range(10, -1, -1):
        print(r)
        sleep(0.2)
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
    for i in range(1, 501, 2):
        if i % 3 == 0:
            soma += i
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
def progressaoAritmetica():
    primeiroTermo = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    decimoTermo = primeiroTermo + (10 - 1) * razao
    for n in range(primeiroTermo, decimoTermo + razao, razao):
        print(f'{n}', end=' ')
# progressaoAritmetica()

# 52. ler um inteiro e dizer se ele é primo (divisível por ele mesmo e por 1)
def nPrimo():
    primo = int(input('Digite um nº: '))
    totDivisivel = 0
    if primo == 0 or primo == 1:
        print('0 e 1 não são considerados nºs primos')
        return

    for c in range(1, primo + 1):
        if primo % c == 0:
            print(f'\033[33m{c} ', end='')
            totDivisivel += 1
        else:
            print(f'\033[31m{c} ', end='')

    print(f'\n\033[97mO nº{primo} foi divisível {totDivisivel} vezes')
    if totDivisivel > 2:
        print('ele não é primo')
    else:
        print('ele é primo')
        # if primo % 1 == 0 and primo % primo == 0:
        #     print('Ele é primo')
nPrimo()

# 53. Assistir à aula
def palidromo():
    frase = str(input('Digite uma frase: '))
    frase = frase.strip().lower()

    if frase == frase[::-1]: #[::1] técnica de slicing em python. Está pegando a string de ponta a ponta (::) com o passo de -1, invertendo a ordem dos caracteres
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
def desafio56():
    totalIdade = 0
    homemMaiorIdade = 0
    nomeHomemMaisVelho = ""
    mulheresMenosDe20 = 0

    for p in range(0, 4):
        nome = input('Qual o seu nome? ').lower()
        idade = int(input('Qual a sua idade? '))
        sexo = input('Qual o seu sexo? ').lower()
        totalIdade += idade

        if sexo == 'fem' and idade < 20:
            mulheresMenosDe20 = mulheresMenosDe20 + 1

        if sexo == 'masc' and idade > homemMaiorIdade:
            homemMaiorIdade = idade
            nomeHomemMaisVelho = nome

    mediaIdade = totalIdade / 2
    print(f'A média de idade do grupo é {mediaIdade}')
    print(f'O nome do homem mais velho é {nomeHomemMaisVelho}')
    print(f'Quantidade de mulheres com menos de 20 anos: {mulheresMenosDe20}')
# desafio56()