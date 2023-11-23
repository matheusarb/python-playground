# FUNÇÕES E MÉTODOS

# 1. funções sem parâmetro
def linha():
    print('-' * 30)


# linha()
# print('Hello world')


# 2. funções com parâmetro
# 2.1. em python, o parâmetro pode ser tipado ou não


def titulo(texto: str):
    print('-' * 30)
    print(f'{texto:^30}')
    print('-' * 30)


# titulo('Teste titulo')


def soma(a: int, b: int):
    print(f'A = {a} e B = {b}')
    r = a + b
    print(f'A soma A + B = {r}')


# soma(4, 5)
# soma(b=20, a=30)


# 3. Funções com quantidade de parâmetros indefinidos:
# o asterisco significa desempacotar (passar vários parâmetros indefinidamente)
# isso significa pegar todos os parâmetros e jogar dentro do parâmetro declarado com *
# no exemplo abaixo, jogar todos os inteiros dentro de num
# isso ira cospir uma TUPLA
def contador(*num):
    tamanho = len(num)
    print(f'recebi os valores ', end='')
    for v in num:
        print(f'{v} ', end='')
    print(f'e são ao todo {tamanho} números')
    print('FIM!')


# contador(1, 2, 5, 3, 9)



# 4. Ao invés de tupla, pode ser feito com lista
# até para facilitar a manipulação dos dados

def dobraValores(lista: list):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)

def dobraValores2(lista: list):
    for i, v in enumerate(lista):
        lista[i] *= 2
    print(lista)

vals = [2, 4, 6, 8, 10]
val1 = vals[:]
dobraValores(val1)
dobraValores2(vals)