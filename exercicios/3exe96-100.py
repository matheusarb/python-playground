from time import sleep

def titulo(txt: str):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)
def lin():
    print('-='*30)

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
    length = len(txt) + 8
    print('~'*length)
    print(f'{txt:^{length}}')
    print('~'*length)
# escreva('Olá, mundo')
# escreva('Matheus')


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
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')


# contador()

# 99. função 'maior' recebendo vários nºs e dizer qual é o maior
def maior(*num):
    print('Analisando os valores passados')
    sleep(0.7)
    m = 0
    for i in num:
        print(f'{i} ', end='')
        if i == 0:
            m = i
        else:
            if i > m:
                m = i
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior é o {m}')


# maior(2, 3, 4, 1, 7, 10, 9, 8)


# 100. criar uma lista e passar duas funções:
# a) uma vai sortear 5 nºs e colocar nela
# b) a outra mostra a soma dos valores pares sorteados
def sorteioepares():
