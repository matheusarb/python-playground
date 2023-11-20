# 78. Ler 5 valores e guardar em lista
# mostrar a) maior e menor em suas respectivas posições
# incompleto para a hipótese de número repetido em múltiplas posições
def lerValores():
    lista = list()
    maior = menor = 0
    for n in range(0,5):
        lista.append(int(input('Digite um valor: ')))

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

    print(f'Maior é {maior} nas posições ', end='')
    for i, v in enumerate(lista):
        if v == maior:
            print(f'{i}... ', end='')
    print()
    print(f'Menor é {menor} nas posições ', end='')
    for i, v in enumerate(lista):
        if v == menor:
            print(f'{i}... ', end='')
    print()
# lerValores()

# 79. vários valores e cadastra em lista. Se já existir, não será adicionado.
# No final exibe os valores únicos em ordem crescente
def mostrarUnicos():
    lista = list()
    while True:
        n = int(input('Cadastre um nº inteiro: '))
        if n not in lista:
            lista.append(n)
        else:
            print('Valor duplicado não será adicionado')

        continua = input('Deseja continuar? [S/N]').strip().lower()

        if continua == 'n':
            break

    lista.sort()
    print(f'Vc digitou os valores {lista}')
# mostrarUnicos()

# 80. digita 5 valores e cadastra em uma lista já na posição correta de inserção (sem usar sort())
def posicaoCorreta():
    lista = list()
    n = int(input('Cadastre um nº inteiro: '))
    lista.append(n)

    while len(lista) < 5:
        menor = min(lista)
        maior = max(lista)
        n = int(input('Cadastre um nº inteiro: '))
        if n < menor:
            lista.insert(lista.index(menor), n)

        if n > maior:
            lista.append(n)

    print(f'Os valores digitados em ordem foram {lista}')
# posicaoCorreta()

# 81. ler nºs e colocar numa lista. Depois, mostre:
# a) Quantos números digitados; b) lista em ordem decrescente; c) Se o valor 5 foi digitado e está ou n
def listaNums():
    lista = list()
    numDigitados = 0

    while True:
        lista.append(int(input('Cadastre um nº inteiro: ')))
        numDigitados += 1


        continua = input('Deseja continuar? [S/N]').strip().lower()
        if continua == 'n':
            break

    print(f'Nºs digitados: {numDigitados}')
    lista.sort(reverse=True)
    print(f'Lista decrescente: {lista}')
    if 5 in lista:
        print(f'O valor 5 foi digitado e está na lista')
    else:
        print(f'O valor 5 não foi digitado')
# listaNums()

# 82. ler nºs e colocar em uma lista. Após:
# a) Criar duas listas extras, uma par e outra impar; b) cada lista é única
def listasParImpar():
    lista = list()
    listaPar = list()
    listaImpar = list()

    while True:
        n = int(input('Cadastre um nº inteiro: '))
        lista.append(n)

        if n % 2 == 0:
            listaPar.append(n)
        elif n % 2 != 0:
            listaImpar.append(n)

        continua = input('Deseja continuar? [S/N]').strip().lower()
        if continua == 'n':
            break
    print(f'lista padrão: {lista}')
    print(f'lista Par: {listaPar}')
    print(f'lista Impar: {listaImpar}')
# listasParImpar()

# 83. verificar se