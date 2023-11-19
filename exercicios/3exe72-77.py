from random import randint

# 72. Criar tupla de 0 a 20 pra, de acordo com input, escrever ele por extenso
def numExtenso():
    numeros = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze',
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    num = int(input('Digite um número de 0 a 20: '))

    while num > 20 or num < 0:
        num = int(input('Valor incorreto. Digite um número de 0 a 20: '))

    print(f'Você digitou o nº {numeros[num]}')
# numExtenso()

# 73. Criar tupla com os times do brasileirao na ordem de colocação. Depois mostre:
# a) 5 primeiros; b) últimos 4; c) lista em ordem alfabética; d) posição do Bahia
def brasileirao():
    tabela = ('Palmeiras', 'Botafogo', 'Gremio', 'Bragantino',
              'Atletico-MG', 'Flamengo', 'Athletico-PR', 'Fluminense',
              'Bahia', 'São Paulo')
    print('-='*20)

    print(f'{tabela[:5]}')
    print(f'{tabela[-4:]}')
    print(f'Times em ordem alfab:\n{sorted(tabela)}')
    for pos, time in enumerate(tabela):
        if time == 'Bahia':
            print(f'o bahia está na {pos+1} posição')
    print(f'Palmeiras está na {tabela.index("Palmeiras") + 1}ª posição')
# brasileirao()

# 74. gerar 5 nºs aleatórios e colocar em uma tupla
# mostrar: a) lista dos nºs; b) maior valor e menor valor
def numAleatorios():
    tupla = (randint(0,10), randint(0,10), randint(0,10),
             randint(0,10), randint(0,10))
    print(f'os valores sorteados foram: ', end='')
    for val in tupla:
        print(f'{val} ', end='')
    sortedTupla = sorted(tupla)
    print(f'\nO maior valor foi: {sortedTupla[-1]}')
    print(f'O menor valor foi: {sortedTupla[0]}')
    print(f'\nO maior valor foi: {max(tupla)}')
    print(f'O menor valor foi: {min(tupla)}')
# numAleatorios()

# 75. ler 4 valores e guardá-los na tupla
# a) quantas vezes o 9 apareceu; b) posição do 1º valor 3; c) quais foram os números pares
# feito usando List
def tuplaPlay():
    tupla = (int(input('digite um nº de 0 a 10: ')), int(input('digite um nº de 0 a 10: ')),
             int(input('digite um nº de 0 a 10: ')), int(input('digite um nº de 0 a 10: ')))
    nove = 0
    posicao3 = 0
    pos = 0
    pares = []

    for pos, n in enumerate(tupla):
        if n == 9:
            nove += 1

        if n == 3:
            posicao3 = pos

        if n % 2 == 0:
            pares.append(n)

    print(f'vc digitou os valores {tupla}')
    print(f'O 9 apareceu {nove} vez(es)')
    print(f'O 9 apareceu {tupla.count(9)} vez(es)')
    print(f'O 3 apareceu na {posicao3}ª posição pela 1ª vez')
    if 3 in tupla:
        print(f'O 3 apareceu na {tupla.index(3)}ª posição pela 1ª vez')
    print(f'os pares são: {pares}')
    print('Os nºs pares são: ', end='')
    for num in tupla:
        if num % 2 == 0:
            print(f'{num} ', end='')
# tuplaPlay()

# 76. tupla com nome de produtos e seus respectivos preços
# organize de forma tabular
def produtosOrg():
    produtos = ('Tv', 2000.23,
                'Jogo', 500.90,
                'caneta', 10.87)

    print('-='*20)
    print(f'{"Lista dos Produtos":^40}')
    print('-='*20)
    for items in range(0, len(produtos), 2):
        print(f'{produtos[items]:.<20} R$ {produtos[items + 1]:>7.2f}')
# produtosOrg()

# 77. tupla com várias palavras
def vogais():
    palavras = ('pao', 'azeite', 'camarao')

    for palavra in palavras:
        print(f'\nna palavra {palavra} temos ', end='')
        for vogais in palavra:
            if vogais.lower() in 'aeiou':
                print(vogais, end=' ')
vogais()