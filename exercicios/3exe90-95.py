import datetime
import sys
from random import randint
from time import sleep
from operator import itemgetter

# 90. ler nome e média de UM aluno, guardando em um dic. Mostrar
def aprovacao():
    aluno = {}

    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
    aluno['situacao'] = ''
    print(f'Nome é {aluno["nome"]}')
    print(f'Média é {aluno["media"]}')

    if aluno['media'] > 5.9:
        aluno['situacao'] = 'Aprovado'
        print(f'Situação é igual a {aluno["situacao"]}')
    else:
        aluno['situacao'] = 'Reprovado'
        print(f'Situação é igual a {aluno["situacao"]}')
# aprovacao()
    #
def aprovacao2():
    aluno = {}

    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
    aluno['situacao'] = ''

    if aluno['media'] > 7:
        aluno['situacao'] = 'Aprovado'
    elif 5.9 < aluno['media'] < 7:
        aluno['situacao'] = 'Em recuperação'
    else:
        aluno['situacao'] = 'Reprovado'

    print('-='*30)
    for k, v in aluno.items():
        print(f' - {k} é {v}')
# aprovacao2()

# 91. 4 players jogam um dado com resultados aleatórios. Guarde os dados em um dic
# a) Mostre os valores sorteados; b) Ranking em ordem decrescente
# incompleto
def scoreJogo():
    partida = list()
    jogador = dict()

    for c in range(0, 4):
        jogador['player'] = str(input('Nome: '))
        jogador['score'] = randint(0, 10)
        partida.append(jogador.copy())

    print('Valores sorteados:')
    for pos in range(0, len(partida)):
        print(f'    O {partida[pos]["player"]} marcou {partida[pos]["score"]} pontos')

    print('Ranking dos jogadores:')
    for c in range(0, len(partida)):
        print(f'{c}º lugar: ')
# scoreJogo()

# 91. 4 players jogam um dado com resultados aleatórios. Guarde os dados em um dic
# a) Mostre os valores sorteados; b) Ranking em ordem decrescente
def scoreJogo2():
    jogadores = {
        'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
    }
    ranking = list()
    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

    print('VALORES SORTEADOS:')
    for k, v in jogadores.items():
        print(f'{k} tirou {v}')
    print('-='*30)
    print('RANKING JOGADORES:')
    for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
# scoreJogo2()

# 92. ler nome, ano nasc e CTPS
# a) adicionar a um dicionário se a CTPS for != de 0
# b) adicionar data de contratação
def trabalhador():
    trabalhador = dict()

    trabalhador['nome'] = str(input('Nome: '))
    trabalhador['idade'] = int(input('Ano nasc: '))
    trabalhador['CTPS'] = int(input('Nº CTPS (0 não tem): '))

    if trabalhador['CTPS'] == 0:
        print(trabalhador)
        print(f'nome tem o valor de {trabalhador["nome"]}')
        print(f'idade tem o valor de {trabalhador["idade"]}')
        print(f'ctps tem o valor de {trabalhador["CTPS"]}')

    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = int(input('Salário: '))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] - trabalhador['idade']) + 35


    print(trabalhador)
    print(f'nome tem o valor de {trabalhador["nome"]}')
    print(f'idade tem o valor de {trabalhador["idade"]}')
    print(f'ctps tem o valor de {trabalhador["CTPS"]}')
    print(f'contratação tem o valor de {trabalhador["contratacao"]}')
    print(f'salário tem o valor de {trabalhador["salario"]}')
    print(f'aposentadoria tem o valor de {trabalhador["aposentadoria"]}')
# trabalhador()

# 93. Aproveitamento jogador.
# armazenar em um dicionário:
# a) nome; b) partidas jogadas; c) gols feitos por partida; d) gols total no campeonato
def desempenhoJogador():
    desempenho = {}
    desempenho['nome'] = str(input('Nome: '))
    desempenho['partidas'] = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
    desempenho['golsPorPartida'] = []
    for p in range(0, desempenho['partidas']):
        desempenho['golsPorPartida'].append(int(input(f'Quantos gols na partida {p}? ')))

    golsTotais = 0
    for gols in desempenho['golsPorPartida']:
        golsTotais += gols
    desempenho['totalGols'] = golsTotais

    print('-='*30)
    print(f'{desempenho}')
    print('-='*30)
    print(f'O campo nome tem o valor {desempenho["nome"]}')
    print(f'O campo gols tem o valor {desempenho["golsPorPartida"]}')
    print(f'O campo total tem o valor {desempenho["totalGols"]}')
    print('-='*30)

    print(f'O jogador {desempenho["nome"]} jogou {desempenho["partidas"]} partidas.')
    for p in range(0, desempenho['partidas']):
        print(f'Na partida {p}, fez {desempenho["golsPorPartida"][p]} gols.')
    print(f'Foi um total de {desempenho["totalGols"]} gols.')
# desempenhoJogador()

# 94. nome sexo e idade de n pessoas. Cada um é um dictionary armazenando todos em uma lista
# Mostrar: a) Quantidade cadastradas; b) Média de idade do grupo
# c) Lista das mulheres; d) Lista de pessoas com idade acima da média
def cadastroPessoas():
    listaPessoas = list()
    pessoa = dict()
    listaMulheres = list()
    acimaMedia = list()
    cadastrados = mediaIdade = 0

    while True:
        pessoa['nome'] = str(input('Nome: '))
        pessoa['idade'] = int(input('Idade: '))

        pessoa['sexo'] = str(input('Sexo [M/F]: '))
        while pessoa['sexo'] not in 'MmFf':
            pessoa['sexo'] = str(input('ERRO! Digite apenas M ou F: '))

        if pessoa['sexo'] in 'Ff':
            listaMulheres.append(pessoa.copy())
        cadastrados += 1

        listaPessoas.append(pessoa.copy())
        pessoa.clear()

        resp = str(input('Deseja cadastrar mais alguém? [S/N]'))
        while resp not in 'SsNn':
            resp = str(input('ERRO! Digite apenas S ou N: '))

        if resp in 'Nn':
            break

    for p in listaPessoas:
        mediaIdade += p['idade']
    mediaIdade = mediaIdade / len(listaPessoas)

    for p in listaPessoas:
        if p['idade'] > mediaIdade:
            acimaMedia.append(p)

    print(f'Nº de cadastrados foi de {cadastrados} pessoas')
    print(f'A média de idade é {mediaIdade:.2f} anos')
    print(f'Lista de mulheres: {listaMulheres}')
    print(f'Lista das pessoas com idade acima da média{acimaMedia}')
cadastroPessoas()

# 95.
def desempenhoJogador2():
    desempenho = {}
    listaJogadores = list()

    while True:
        desempenho['nome'] = str(input('Nome: '))
        desempenho['partidas'] = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
        desempenho['golsPorPartida'] = []

        for p in range(0, desempenho['partidas']):
            desempenho['golsPorPartida'].append(int(input(f'Quantos gols na partida {p}? ')))

        desempenho['golsTotais'] = 0
        for gol in desempenho['golsPorPartida']:
            desempenho['golsTotais'] += gol

        listaJogadores.append(desempenho.copy())
        desempenho.clear()
        print('-'*30)

        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break


    print('-='*30)
    print(f'cod     nome      gols       total')
    for pos, jog in enumerate(listaJogadores):
        print(f'{pos}    {jog["nome"]}    {jog["golsPorPartida"]}    {jog["golsTotais"]}')
    print('-='*30)

    dadosJogador = int(input('Mostrar dados de qual jogador?' ))
    while True:
        for dadosJogador, jog in enumerate(listaJogadores):
            print(f'-- LEVANTAMENTO DE {jog["nome"]}: ')
            for count in range(0, len(dadosJogador['golsPorPartida'])):
                print(f'No jogo {count} fez ')
# desempenhoJogador2()