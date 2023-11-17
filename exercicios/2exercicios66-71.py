import os
from random import randint

os.system('cls' if os.name == 'nt' else 'clear') # limpar console

# 66. mostrar soma dos números e contador. Condição de parada = 999
def somaEContador():
    soma = contador = 0
    num = int(input('Digite um nº: '))

    if num == 999:
        print('Vc saiu do programa sem fazer soma alguma.')
    else:
        soma += num
        contador += 1

        while num != 999:
            num = int(input('Digite um nº: '))
            if num == 999:
                break
            soma += num
            contador += 1

    print(f'A soma deu {soma} e a quantidade de nºs foi de {contador}')
# somaEContador()

def somaEContador2():
    soma = count = num = 0

    while True:
        num = int(input('Digite um nº: '))
        if num == 999:
            break
        soma += num
        count += 1
    print(f'A soma é {soma} e a qntidade de nºs usados foi {count}')
# somaEContador2()

# 67. Tabuada pra vários inputs diferentes
def tabuadaMultipla():
    num = 0
    count = 1

    while True:
        count = 1
        print('-' * 30)
        num = int(input('Quer ver a tabuada de qual valor?: '))
        print('-' * 30)

        if num >= 0:
            while count < 11:
                print(f'{num} * {count} = {num*count}')
                count += 1
        else:
            print('FIM das tabuadas')
# tabuadaMultipla()

def tabuadaMultipla2():
    while True:
        n = int(input('digite nº: '))
        print('-'*30)

        if n < 0:
            break

        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')

        print('-'*30)
    print('Fim das tabuadas')
tabuadaMultipla2()

# 68. jogo do par ou ímpar
def parOuImpar():
    vitorias = 0

    while True:
        jogador = input('Par[0] ou ímpar[1]? ').strip().lower()
        resultado = randint(0, 20)

        if jogador == 'par' or jogador == '0':
            if resultado % 2 == 0:
                print(f'Você jogou ')
                print(f'Você venceu!')
                vitorias += 1
            elif resultado % 2 != 0:
                print(f'Você perdeu :(\nVitórias consecutivas: {vitorias}')
                break

        if jogador == 'impar' or jogador == '1':
            if resultado % 2 != 0:
                print(f'Você venceu!')
                vitorias += 1
            elif resultado % 2 == 0:
                print(f'Você perdeu :(\nVitórias consecutivas: {vitorias}')
                break
# parOuImpar()

def parOuImpar2():
    vitorias = 0

    while True:
        total = 0
        print('*'*10)
        print(' Par ou Ímpar ')
        print('*'*10)
        numJogador = int(input('Digite um nº entre 0 e 10: '))
        computador = randint(0,10)
        escolhaJogador = input('Pár ou Ímpar? [P/I]').strip().lower()

        total = numJogador + computador

        if escolhaJogador == 'p':
            print('-'*10)
            if total % 2 == 0:
                print(f'Vc jogou {numJogador} e o computador {computador}. Total deu {total} e é PAR.\nVc GANHOU!')
                vitorias += 1
                print('-' * 10)
            elif total % 2 != 0:
                print(f'Vc jogou {numJogador} e o computador {computador}. Total deu {total} e é IMPAR.\nVocê PERDEU')
                print(f'Total de vitorias: {vitorias}')
                print('-' * 10)
                break

        if escolhaJogador == 'i':
            print('-' * 10)
            if total % 2 != 0:
                print(f'Vc jogou {numJogador} e o computador {computador}. Total deu {total} e é IMPAR.\nVc GANHOU')
                vitorias += 1
                print('-' * 10)
            elif total % 2 == 0:
                print(f'Vc jogou {numJogador} e o computador {computador}. Total deu {total} e é PAR.\nVc PERDEU')
                print(f'Total de vitorias: {vitorias}')
                print('-' * 10)
                break
# parOuImpar2()

# 69. ler idade e sexo de várias pessoas
def cadastro():
    maiores = homens = mulheresMenos20 = 0

    while True:
        idade = int(input('Qual a sua idade? '))
        sexo = input('Qual o seu sexo? [M/F] ').strip().lower()
        while sexo not in 'mf':
            sexo = input('Qual o seu sexo? [M/F] ').strip().lower()

        if sexo == 'm':
            homens += 1
            if idade > 17:
                maiores += 1

        if sexo == 'f':
            if 17 < idade < 20:
                mulheresMenos20 += 1
                maiores += 1
            elif idade < 20:
                mulheresMenos20 += 1

        continuar = input('Deseja continuar? [S/N]').strip().lower()
        if continuar == 'n':
            break
    print('-'*10)
    print(f'\nMaiores de 18 anos: {maiores}')
    print(f'Quantidade de homens: {homens}')
    print(f'Mulheres com menos de 20 anos: {mulheresMenos20}')
# cadastro()

# 70. ler nome e preco de varios produtos e mostrar: 1.Total gasto na compra 2.produtos q custam + de 1k 3.Nome produto + barato
def compra():
    totalCompra = 0.0
    maisDe1000 = 0
    maisBarato = ''
    precoMaisBarato = 0

    while True:
        nomeProduto = input('Qual o nome do produto? ')
        preco = float(input('Qual o preco dele? R$'))


        if precoMaisBarato == 0:
            precoMaisBarato = preco
        elif preco < precoMaisBarato:
            precoMaisBarato = preco
            maisBarato = nomeProduto

        if preco > 1000:
            maisDe1000 += 1

        totalCompra += preco

        continuar = input('Deseja continuar a compra? [S/N] ').strip().lower()
        if continuar == 'n':
            break

    print('-'*10)
    print(f'Total da compra: {totalCompra:.2f}')
    print(f'Produtos + de 1.000 reais: {maisDe1000}')
    print(f'Produto mais barato: {maisBarato}')
# compra()

# 71. Caixa Eletrônico. 1. Valor a ser sacado(int) 2. Programa indica quantas cédulas de cada valor serão entregues
# cédulas de: 50, 20, 10, 1
def caixaEletronico1():
    saque = int(input('Digite o valor a ser sacado: '))
    nota50 = nota20 = nota10 = nota1 = 0
    valorDeduzido = 0

    if saque > 0:
        while saque != 0:
            if saque % 2 == 0:
                while saque % 50 == 0:
                    nota50 += 1
                    saque = saque - (saque / 2)

            while saque % 20 == 0:
                nota20 += 1
                saque -= (saque / 5)

            while saque % 10 == 0:
                nota10 += 1
                saque -= (saque / 10)

            while saque % 1 == 0:
                nota1 += 1
                saque -= (saque / 100)

    print(f'Total de {nota50} cédulas de R$ 50')
    print(f'Total de {nota20} cédulas de R$ 20')
    print(f'Total de {nota10} cédulas de R$ 10')
    print(f'Total de {nota1} cédulas de R$ 10')
# caixaEletronico1()

def caixaEletronico2():
    saque = int(input('Digite o valor a ser sacado: '))
    nota50 = nota20 = nota10 = nota1 = 0
    valorDeduzido = 0

    if saque > 0:
        while saque != 0:
            if saque % 2 == 0:
                while saque % 50 == 0:
                    nota50 += 1
                    saque = saque - (saque / 2)

            while saque % 20 == 0:
                nota20 += 1
                saque -= (saque / 5)

            while saque % 10 == 0:
                nota10 += 1
                saque -= (saque / 10)

            while saque % 1 == 0:
                nota1 += 1
                saque -= (saque / 100)

    print(f'Total de {nota50} cédulas de R$ 50')
    print(f'Total de {nota20} cédulas de R$ 20')
    print(f'Total de {nota10} cédulas de R$ 10')
    print(f'Total de {nota1} cédulas de R$ 10')
# caixaEletronico2()