# 78. Ler 5 valores e guardar em lista
# mostrar a) maior e menor em suas respectivas posições
def lerValores():
    lista = list()
    maior = menor = 0
    for n in range(0,5):
        lista.append(int(input('Digite um valor a partir de 1: ')))

    # duas formas de resolver:

    # 1ª mais preguiçosa DEU CERTO

    # print(f'O maior é {max(lista)} na posição {lista.index(max(lista))}')
    # print(f'O menor é {min(lista)} na posição {lista.index(min(lista))}')

    # 2ª usando enumerate DEU CERTO
    posMaior = posMenor = 0
    for pos, n in enumerate(lista):
        if pos == 0:
            maior = n
            menor = n
        if n > maior:
            maior = n
            posMaior = pos
        if n < menor:
            menor = n
            posMenor = pos
    print(f'Maior é {maior} na posição {posMaior}')
    print(f'Menor é {menor} na posição {posMenor}')
lerValores()

# 79.