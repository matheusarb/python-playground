import os

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

# 67. tabuada pra vários inputs diferentes
def tabuadaMultipla():
    num = 0
    count = 1

    while True:
        count = 1
        num = int(input('Digite um nº: '))

        if num >= 0:
            while count < 11:
                print(f'{num} * {count} = {num*count}')
                count += 1
        else:
            print('FIM')
# tabuadaMultipla()

# 68.