from time import sleep
from random import randint


def titulo(txt: str):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


def lin():
    print('-=' * 30)


# 96. uma função para calcular a área do terreno
def areaTerreno():
    titulo('Controle de Terrenos')

    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))

    def calcularArea(largura, comprimento):
        a = l * c
        return a

    print(f'A área de um terreno {l} x {c} é de {calcularArea(l, c)}m²')


# areaTerreno()


# 97. função 'escreva' que recebe texto e mostre msg com tamanho adaptável(??)
def escreva(txt: str):
    length = len(txt) + 4
    print('~' * length)
    print(f'{txt:^{length}}')
    print('~' * length)


# escreva('Olá, mudo')

def escreva2(msg):
    length = len(msg) + 4
    print('~'*length)
    print(f'  {msg}')
    print('~'*length)


# escreva2('Olá, mudo')

# 98. função 'contador' recebe 3 parâmetros (início, fim, passo)
# Contar a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada

def contador():
    lin()
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        print(i, end=' ')
    print('FIM!')
    lin()

    lin()
    print('Contagem de 10 até 0 de 2 em 2:')
    for i in range(10, -1, -2):
        print(i, end=' ')
    print('FIM!')
    lin()

    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    if inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.2)
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(0.2)
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.2)
    print('FIM!')

# contador()


# 99. função 'maior' recebendo vários nºs e dizer qual é o maior
def maior(* num):
    print('Analisando os valores passados...')
    sleep(0.4)
    m = 0
    for valor in num:
        print(f'{valor} ', end='')
        if valor == 0:
            m = valor
        else:
            if valor > m:
                m = valor
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior é o {m}')


# maior(2, 3, 4, 1, 7, 10, 9, 8)


def maior2(* num):
    titulo('Maior Nº')
    m = 0
    length = len(num)
    if length == 0:
        print('Lista de nºs vazia')
    else:
        for val in num:
            print(val, end=' ')
        print()
        print(f'Foram informados {length} números. O maior é o {max(num)}')


# maior2(2, 3, 7, 1, 0, 12, 9, 32, 89, 4)


# 100. criar uma lista e passar duas funções:
# a) uma vai sortear 5 nºs e colocar nela
# b) a outra mostra a soma dos valores pares sorteados
def sorteioepares():
    numeros = list()

    def sorteio(lista: list):
        count = 0
        print('Os nºs sorteados são: ', end='')
        while count < 5:
            n = randint(0, 10)
            lista.append(n)
            print(n, end=' ')
            count += 1
        return lista

    sorteio(numeros)

    print()

    def somaPar(lista: list):
        soma = 0
        print(f'Os valores pares são: ', end='')
        for n in lista:
            if n % 2 == 0:
                print(n, end=' ')
                soma += n
        print()
        print(f'A soma dos valores pares é: {soma}')

    somaPar(numeros)


sorteioepares()
