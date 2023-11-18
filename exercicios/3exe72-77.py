# 72. Criar tupla de 0 a 20 pra, de acordo com input, escrever ele por extenso
def numExtenso():
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    num = int(input('Digite um número de 0 a 20: '))

    while num > 20 or num < 0:
        num = int(input('Valor incorreto. Digite um número de 0 a 20: '))

    print(f'Você digitou o nº {numeros[num]}')
numExtenso()