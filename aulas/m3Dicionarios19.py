# DICIONÁRIOS
# São identificados por chaves

#Declarar dicionários:
dict1 = dict()
dict2 = {}

dados = {'Nome': 'Pedro',
         'Idade': 25
         }
# print(dados['nome'])
# print(dados['idade'])
# dados['sexo'] = 'M'
# print(dados['sexo'])
# del dados['idade']
#
# print(dados.values())
# print(dados.keys())
t = dados.get('nome')
# print(t)
# print(dados.items())
# print(dados)
#
# for k, v in dados.items():
#     print(f'{k} é {v}')

#Prática
# dicionário simples
pessoas = {'nome': 'Matheus',
           'idade': 31,
           'sexo': 'Masc'
          }

# acessar Valores no dicionário
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(f'O {pessoas.get("nome")}')

# acessar chaves:
# print(pessoas.keys())

# acessar apenas chaves (USAR LAÇO)
# for k in pessoas.keys():
#     print(k, end=' ')
# print()

# acessar apenas values (USAR LAÇO)
# for v in pessoas.values():
#     print(v, end=' ')
# print()

# acessar items do dicionário
# ele cospe uma lista, contendo x tuplas que compõe cada chave-valor do dicionário:
# print(pessoas.items())

# acessar todo_ o item (chave-valor) (USAR LAÇO)
# for k, v in pessoas.items():
#     print(k, v)

# adicionar elementos (NÃO PRECISA DE APPEND(), É SÓ ADD UMA CHAVE NA BRACKET NOTATION)
# precisa inicializar com um valor
pessoas['peso'] = 75
print(pessoas.keys())

# criar dicionário dentro de lista:
listaEstadoCapital = list()
estado1 = {'UF': 'BA', 'Capital': 'Salvador'}
estado2 = {'UF': 'SP', 'Capital': 'São Paulo'}
listaEstadoCapital.append(estado1)
listaEstadoCapital.append(estado2)
print(listaEstadoCapital)



# print(listaEstadoCapital[0]['Capital'])
# print(listaEstadoCapital)

# for i in listaEstadoCapital:
#     for k, v in i.items():
#         print(f'{k} = {v}')

for i in listaEstadoCapital:
    for val in i.values():
        print(f'{val}', end =' ')
    print()

# adicionar dicionário a uma lista dinamicamente:

avengers = list()
heroi = dict()
# for c in range (0, 2):
#     heroi['nome'] = str(input('Nome do herói: '))
#     heroi['poder'] = str(input('Poder do herói: '))
#     avengers.append(heroi.copy())

# print(avengers)