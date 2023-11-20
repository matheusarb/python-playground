from random import randint

# 84. ler nome e peso de várias pessoas guardando em uma lista. Ao fim, mostre:
# a) quantidade de cadastros (len da lista composta); b) lista com as pessoas mais pesadas c) pessoas mais leves
def pessoasPesadasLeves():
    dados = list()
    pessoas = list()
    contagem = maiorPeso = menorPeso = 0

    # cadastrar pessoas
    while True:
        dados.append(str(input('Digite seu nome: ')))
        dados.append(int(input('Digite seu peso: ')))
        pessoas.append(dados[:])
        contagem += 1
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

    # print(f'Pessoas cadastradas: {contagem}')

    print(f'O maior peso foi de {maiorPeso}kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == maiorPeso:
            print(f'{v[0]} ', end='')
    print()
    print(f'O menor peso foi de {menorPeso}kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == menorPeso:
            print(f'{v[0]} ', end='')
    print()
# pessoasPesadasLeves()

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

# 87. Aprimorar o anterior e mostrar:
# a) soma dos pares; b) soma dos vals da 3ª coluna; c) Maior valor da segunda linha
# incompleto
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

# 88. rodar n sorteios da megasena de acordo com o input do usuário
def megasena():
    numeroJogos = int(input('Qntos jogos quer sortear? '))
    jogo = 1
    numerosPremiados = list()
    print('-='*3 + f'SORTEANDO {numeroJogos} JOGOS' + '-='*3)

    for sort in range(0, numeroJogos):
        numerosPremiados.clear()
        for n in range(0, 6):
            numerosPremiados.append(randint(1, 60))
        print(f'Jogo {jogo}: {numerosPremiados}')
        jogo += 1
# megasena()

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