from random import randint

# 84. ler nome e peso de várias pessoas guardando em uma lista. Ao fim, mostre:
# a) quantidade de cadastros (len da lista composta); b) lista com as pessoas mais pesadas c) pessoas mais leves
def pessoasPesadasLeves():
    dados = list()
    pessoas = list()
    maiorPeso = menorPeso = 0

    # cadastrar pessoas
    while True:
        dados.append(str(input('Digite seu nome: ')))
        dados.append(float(input('Digite seu peso: ')))
        pessoas.append(dados[:])
        dados.clear()

        resp = input('deseja continuar? [S/N]')
        if resp in 'Nn':
            break

    # descobrir maior e menor peso
    for i, v in enumerate(pessoas):
        if i == 0:
            menorPeso = v[1]
        if v[1] > maiorPeso:
            maiorPeso = v[1]
        if v[1] < menorPeso:
            menorPeso = v[1]

    print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
    print(f'O maior peso foi de {maiorPeso}kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == maiorPeso:
            print(f'{v[0]} ', end='')
    print()
    print(f'O menor peso foi de {menorPeso}kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == menorPeso:
            print(f'{v[0]} ', end='')
# pessoasPesadasLeves()

def pesopessoas2():
    #usar temp
    temp = []
    principal = []
    maior = menor = 0

    while True:
        temp.append(str(input('Nome: ')))
        temp.append(int(input('Peso: ')))

        if len(principal) == 0:
            maior = menor = temp[1]
        else:
            if temp[1] > maior:
                maior = temp[1]
            if temp[1] < menor:
                menor = temp[1]

        principal.append(temp[:])
        temp.clear()

        resp = input('deseja continuar? [S/N]')
        if resp in 'Nn':
            break

    print(f'Pessoas cadastradas: {len(principal)}')
    print(f'O maior peso foi de {maior}. Peso de ', end='')
    for p in principal:
        if p[1] == maior:
            print(f'{p[0]} ', end='')
    print(f'O menor peso foi de {menor}. Peso de ', end='')
    print()
    for p in principal:
        if p[1] == menor:
            print(f'{p[0]} ', end='')
# pesopessoas2()

# 85. Lista de pares e ímpares
def listaParesImpares():
    nums = list()
    pares = list()
    impares = list()
    nums.append(pares)
    nums.append(impares)
    print(nums)

    valor = 1
    for n in range(0, 7):
        n = int(input(f'Digite o {valor}º valor: '))

        if n % 2 == 0:
            nums[0].append(n)
        elif n % 2 != 0:
            nums[1].append(n)


    print(f'Valores pares: {nums[0]}')
    print(f'Valores impares: {nums[1]}')
# listaParesImpares()

def listaParesImpares2():
    nums = [[], []]

    for v in range(1, 8):
        n = int(input(f'Digite o {v}º valor: '))

        if n % 2 == 0:
            nums[0].append(n)
        elif n % 2 != 0:
            nums[1].append(n)

    nums[0].sort()
    nums[1].sort()

    print(f'Valores pares: {nums[0]}')
    print(f'Valores impares: {nums[1]}')
# listaParesImpares2()

# 86. Criar matriz 3x3 e mostrar na formatação correta na tela
# deu ruim
def matriz3por3():
    lista = list()
    linha1 = list()
    linha2 = list()
    linha3 = list()
    linha = coluna = 0

    for n in range(0, 3):
        linha = 0
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        coluna += 1
        linha1.append(num)
    lista.append(linha1)

    coluna = 0
    for n in range(0, 3):
        linha = 1
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        coluna += 1
        linha2.append(num)
    lista.append(linha2)

    coluna = 0
    for n in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        linha = 2
        coluna += 1
        linha3.append(num)
    lista.append(linha3)

    return lista
# matriz3por3()

def matriz3por32():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pares = terceiraCol = maiorVal = 0

    for linha in range(0, 3):
        for coluna in range(0, 3):
            matriz[linha][coluna] = int(input('digite um nº: '))
    print('-='*30)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'[{matriz[linha][coluna]:^5}]', end='')

            # soma dos valores pares
            if matriz[linha][coluna] % 2 == 0:
                pares += matriz[linha][coluna]
        print()

    print('-='*30)

    print(f'A soma dos pares é: {pares}')
    # soma dos vals na 3ª coluna
    for l in range(0, 3):
        terceiraCol += matriz[l][2]
    print(f'A soma da 3ª coluna é: {terceiraCol}')
    # maior valor segunda linha
    for c in range(0, 3):
        if c == 0:
            maiorVal = matriz[1][c]
        else:
            if matriz[1][c] > maiorVal:
                maiorVal = matriz[1][c]
    print(f'maior valor da segunda linha é: {maiorVal}')
# matriz3por32()

def matriz2por2():
    matriz = [[0, 0], [0, 0]]

    for l in range(0, 2):
        for c in range(0, 2):
            matriz[l][c] = int(input('Digite um valor: '))

    for l in range(0, 2):
        for c in range(0, 2):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
# matriz2por2()

# 87. Aprimorar o anterior e mostrar:
# a) soma dos pares; b) soma dos vals da 3ª coluna; c) Maior valor da segunda linha
# FEITO NO MATRIZ3POR32
def continuacao():
    lista = matriz3por3()
    pares = 0
    coluna3 = 0
    maiorSegundaLinha = 0
    #soma dos pares
    for i, v in enumerate(lista):
        if v % 2 == 0:
            pares += v
    print(pares)
# continuacao()

def continuacao2():
    matriz = matriz3por32()

    print(f'soma dos valores pares: {pares}')
    print(f'soma dos valores terceira coluna: {terceiraCol}')
    print(f'maior valor segunda linha é {maiorVal}')
# continuacao2()

# 88. rodar n sorteios da megasena de acordo com o input do usuário
def megasena():
    numeroJogos = int(input('Qntos jogos quer sortear? '))
    jogo = 1
    listaNumerosPremiados = list()
    print('-='*3 + f'SORTEANDO {numeroJogos} JOGOS' + '-='*3)

    for sort in range(0, numeroJogos):
        listaNumerosPremiados.clear()
        for n in range(0, 6):
            numPremiado = randint(1, 60)
            if numPremiado not in listaNumerosPremiados:
                listaNumerosPremiados.append(numPremiado)
        listaNumerosPremiados.sort()
        print(f'Jogo {jogo}: {listaNumerosPremiados}')
        jogo += 1
megasena()

# 89. lista com nome e duas notas de todos os alunos
# mais ou menos feito
def alunosEMedia():
    medias = list()
    alunos = list()
    aluno = list()

    while True:
        aluno.clear()
        aluno.append(str(input('Nome: ')))
        aluno.append(int(input('Nota1: ')))
        aluno.append(int(input('Nota2: ')))
        alunos.append(aluno[:])

        resp = input('deseja continuar? [S/N]')
        if resp in 'Nn':
            break

    # for al in alunos:
    #     print(f'{al[0]}: {al[1]} e {al[2]}')

    print(f'No.[:<3]NOME[:5<]MÉDIA')
    for pos, val in enumerate(alunos):
        print(f'{pos:<3} {val[0]:<5} {(val[1] + val[2]) / 2}')

    while True:
        mostrarNota = int(input('Mostrar nota de qual aluno? (999 sai do programa) '))
        if mostrarNota == 999:
            break
        else:
            for pos, v in enumerate(alunos):
                if pos == mostrarNota:
                    print(f'Notas de {v[0]} são {v[1]} e {v[2]}')
# alunosEMedia()