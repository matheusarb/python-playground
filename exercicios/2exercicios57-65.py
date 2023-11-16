import os
import random
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 57. Ler o sexo e aceitar input apenas 'M' ou 'F'
# assistir à resolução
def sexoPessoa():
    sexo = input('Informe o seu sexo [M/F]: ')
    if sexo == 'M':
        print('Vc é homem')
        return
    elif sexo == 'F':
        print('Vc é mulher')
        return

    while sexo != 'M' or sexo != 'F':
        print('Informação inválida. Por favor, digite o seu sexo novamente. [M/F]')
# sexoPessoa()

def sexoPessoa2():
    sexo = input('Informe o seu sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Informação inválida. Informe o seu sexo [M/F]: ').upper()
    if sexo == 'F':
        print('Vc é muié')
    elif sexo == 'M':
        print('vc é homi')
# sexoPessoa2()

# 58. usuário fala um número de 1 a 5, código gera aleatório. Verificar e se dizer se vencey
# Adicionar palpite do usuário
def guessingGame():
  rand = random.randint(0, 10)
  n = int(input('Digite um nº de 0 a 10: '))
  palpite = 0
  print(f'nº sorteado: {rand}')
  if rand == n:
    print(f'Parabéns, vc acertou no palpite de nº {palpite}')
  else:
    print('Tente outra vez.')
    palpite += 1
# guessingGame()

def guessingGame2():
  n = int(input('Digite um nº de 0 a 10: '))
  randomNum = random.randint(0, 10)
  palpite = 0
  print(f'nº sorteado: {randomNum}')
  while n != randomNum:
      randomNum = random.randint(0, 10)
      palpite += 1
  print(f'Vc acertou! Vc levou {palpite} tentativas')
# guessingGame2()

# 59. ler dois valores e fazer
def operacoes():
    n1 = int(input('Digite um nº: '))
    n2 = int(input('Digite um nº: '))
    escolha = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair'))

    while escolha == 4:
        n1 = int(input('Digite um nº: '))
        n2 = int(input('Digite um nº: '))
        escolha = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair'))

    if escolha == 1:
        print(f'O valor da soma é {n1+n2}')
    elif escolha == 2:
        print(f'O valor da multiplicação é {n1 * n2}')
    elif escolha == 3:
        maiorNum = 0
        if n1 > n2:
            maiorNum = n1
        elif n2 > n1:
            maiorNum = n2
        else:
            print(f'os nºs são iguais ({n1} e {n2})')
            return
        print(f'O maior nº é = {maiorNum}')
    elif escolha == 5:
        return
    else:
        print('Opção incorreta. Escolha uma das opções do menu')
        escolha = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair'))
# operacoes()

# 60. Fatorial
def fatorial():
    num = int(input('Digite um nº inteiro: '))
    result = 1
    count = num
    while count != 0:
        result *= count
        count -= 1

    print(f'fatorial de {num} é {result}')
# fatorial()

# 61. Refazer o 51 de PA (pqp)

# 62. Melhorar o 61 (PQP)

# 63. SEQUÊNCIA DE FIBONACCI
# tá errado. Fudeu
def fibonacci():
    nthNum = int(input('digite um nº inteiro: '))
    n1 = 0
    n2 = 1
    fibSeq = []
    index = 2
    while index <= nthNum:
        fibSeq[index] = fibSeq[index - 1] + fibSeq[index - 2]
        index += 1
    print(f'{n1} {n2}', end='')
    print(f'{fibSeq} ')
# fibonacci()

# 64. digitar n números, estabelecer condição de parada em '999', apresentar a soma e a quantidade de nºs digitados
def somaEContador():
    num = int(input('digite um nº: '))
    soma = 0
    count = 0
    if num == 999:
        soma += num
        count += 1
        print(f'foram digitados {count} nºs e a soma é {soma}')

    while num != 999:
        soma += num
        count += 1
        num = int(input('digite um nº: '))
    print(f'foram digitados {count} nºs e a soma é {soma}')
# somaEContador()

# 65. Ler n números. No fim, mostrar a média, qual foi o maior e qual foi o menor valor lido. Sempre perguntar se ele quer continuar
# Tá errado
def mediaEMaiorEMenor():
    num1 = int(input('digite um nº: '))
    counter = 0
    soma = 0
    media = 0
    maiorNum = 0
    menorNum = 0
    resp = input('Você quer continuar? [S/N]').upper()
    if resp == 'N':
        counter += 1
        print(f'Você só digitou um nº e ele foi o {num1}')

    while resp == 'S':
        num = int(input('digite um nº: '))


        if num > maiorNum:
            maiorNum = num

        if menorNum == 0:
            menorNum = num
        elif menorNum > num:
            menorNum = num

        counter += 1
        soma += num
        resp = input('Você quer continuar? [S/N]').upper()

    media = (soma + num1) / counter + 1
    print(f'A média foi de {media}\nmenor valor {menorNum}\nmaior valor {maiorNum}')
# mediaEMaiorEMenor()