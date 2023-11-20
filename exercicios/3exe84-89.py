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
    for p in pessoas:
        if p == 0:
            maiorPeso = p[1]
            menorPeso = p[1]
        else:
            if p[1] > maiorPeso:
                maiorPeso = p[1]
            if p[1] < menorPeso:
                menorPeso = p[1]

    print(f'Pessoas cadastradas: {contagem}')

    print(f'O maior peso foi de {maiorPeso}. Peso de ', end='')
    for index, valor in enumerate(pessoas):
        if index == 0:
            menorPeso = valor[1]
            maiorPeso = valor[1]
        else:
            if valor[1] >= maiorPeso:
                print(f'{valor[0][1]} ', end='')

    # print(f'O menor peso foi de {menorPeso}')
# pessoasPesadasLeves()

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