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
        print('-' * 12)
        num = int(input('Quer ver a tabuada de qual valor?: '))
        print('-' * 12)

        if num >= 0:
            while count < 11:
                print(f'{num} * {count} = {num*count}')
                count += 1
        else:
            print('FIM das tabuadas')
# tabuadaMultipla()

# 68. jogo do par ou ímpar
def parOuImpar():
    vitorias = 0

    while True:
        jogador = input('Par[0] ou ímpar[1]? ').strip().lower()
        resultado = randint(0, 20)

        if jogador == 'par' or jogador == '0':
            if resultado % 2 == 0:
                print(f'Você venceu!')
                vitorias += 1
            elif resultado % 2 != 0:
                print(f'Você perdeu :( Vitórias consecutivas: {vitorias}')
                break

        if jogador == 'impar' or jogador == '1':
            if resultado % 2 != 0:
                print(f'Você venceu!')
                vitorias += 1
            elif resultado % 2 == 0:
                print(f'Você perdeu :( Vitórias consecutivas: {vitorias}')
                break
# parOuImpar()

