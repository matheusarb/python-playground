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
        sexo = input('Informação inválida. Por favor, digite o seu sexo novamente. [M/F]')
# sexoPessoa()

def sexoPessoaGuanabara():
    sexo = input('informe seu sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Informação inválida. Por favor, digite o seu sexo novamente. [M/F]')
    print(f'Sexo {sexo} registrado')
# sexoPessoaGuanabara()

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
def guessingGame2():
  n = int(input('Digite um palpite de 1 a 10: '))
  randomNum = random.randint(0, 10)
  palpite = 0
  # print(f'nº sorteado: {randomNum}')
  while n != randomNum:
      if n > randomNum:
          print(f'Menos... Tente mais uma vez')
          n = int(input('Digite um palpite de 1 a 10: '))
      elif n < randomNum:
          print(f'Mais... Tente mais uma vez')
          n = int(input('Digite um palpite de 1 a 10: '))
      palpite += 1
  print(f'Vc acertou! Vc levou {palpite} tentativas')
# guessingGame2()
def guessingGuanabara():
    print('Pensei em um nº de 0 a 10. Será que você consegue acertar qual foi?')
    numSorteado = random.randint(0, 10)
    acertou = False
    palpites = 0
    while acertou == False:
        numJogador = int(input('Digite o seu palpite entre 0 e 10: '))
        palpites += 1
        if numJogador == numSorteado:
            acertou = True
        else:
            if numJogador > numSorteado:
                print('Menos... tente mais uma vez')
            elif numJogador < numSorteado:
                print('Mais... tente mais uma vez')
    print(f'Vc acertou o número em {palpites} tentativas. Parabéns!')
# guessingGuanabara()

# 59. MENU DE OPÇÕES: ler dois valores e fazer operações
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
    result = num
    count = num - 1
    while count != 0:
        result *= count
        count -= 1
        print(f'{count}', end=' ')

    print(f'fatorial de {num} é {result}')
# fatorial()

# 61. Refazer o 51 de PA (pqp)
def pa():
    primeiroTermo = int(input('Primeiro termo: '))
    razao = int(input('razão da PA: '))
    termo = primeiroTermo
    counter = 0
    while counter <= 10:
        if counter == 10:
            print(f'{termo} -> Pausa', end='')
        else:
            print(f'{termo} -> ', end='')
        termo += razao
        counter += 1
# pa()

# 62. Melhorar o 61 (PQP)
def pa2():
    primeiroTermo = int(input('Primeiro termo: '))
    razao = int(input('razão da PA: '))
    termo = primeiroTermo
    counter = 0
    total = 10
    maisTermos = 0
    while maisTermos != 0:
        total += maisTermos
        while counter <= total:
            if counter == 10:
                print(f'{termo} -> Pausa')

            else:
                print(f'{termo} -> ', end='')
            termo += razao
            counter += 1
# pa2()

# 63. SEQUÊNCIA DE FIBONACCI
# tá errado. Fudeu

def fibonacci():
    print('-'*30)
    print('Sequência de Fibonacci')
    print('-'*30)
    nthNum = int(input('quantos termos vc quer mostrar? '))
    n1 = 0
    n2 = 1
    n3 = 0
    count = 3
    print(f'{n1} {n2} ', end='')
    while count <= nthNum:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(f'{n3} ', end='')
        count += 1
    print('-> Fim')
# fibonacci()

# 64. digitar n números, estabelecer condição de parada em '999', apresentar a soma e a quantidade de nºs digitados
def somaEContador():
    num = int(input('digite um nº: '))
    soma = 0
    count = 0
    if num == 999:
        print(f'Você digitou {num}. O programa irá encerrar sem somar')
        return

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
    counter = 1

    soma = num1
    maiorNum = 0
    menorNum = num1

    resp = input('Você quer continuar? [S/N]').upper()

    if resp == 'N':
        print(f'Você só digitou um nº e ele foi o {num1}')

    while resp == 'S':
        num = int(input('digite um nº: '))
        counter += 1
        soma += num

        if menorNum == 0:
            menorNum = num
        if menorNum > num:
            menorNum = num
        if num > maiorNum:
            maiorNum = num

        resp = input('Você quer continuar? [S/N]').upper()

    media = soma / counter
    print(f'A média foi de {media:.2f}\nmenor valor {menorNum}\nmaior valor {maiorNum}')
# mediaEMaiorEMenor()