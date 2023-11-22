import datetime
import sys
from random import randint
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
        print(f'ctps tem o valor de {trabalhador["ctps"]}')

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

# 94.


