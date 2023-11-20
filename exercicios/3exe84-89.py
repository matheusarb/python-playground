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

    print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == maiorPeso:
            print(f'{v[0]} ', end='')
    print()
    print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end='')
    for i, v in enumerate(pessoas):
        if v[1] == menorPeso:
            print(f'{v[0]} ', end='')
    print()
pessoasPesadasLeves()

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