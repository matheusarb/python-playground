# LISTAS PARTE 2

# LISTAS COMPOSTAS (Listas dentro de listas)
# adicionar estruturas compostas às Listas

dados = []
dados.append('Matheus')
dados.append(10)

pessoas = list()
# lembrar sempre de fazer uma cópia
# LEMBRAR SEMPRE DE FAZER UMA CÓPIA ISSO É MUITO IMPORTANTE
pessoas.append(dados[:])
print(pessoas)
pessoas.append(['Maria', 9])
# print(pessoas)
# print(pessoas[0][0])
# print(pessoas[1][1])

print('-='*30)

teste = []
teste.append('Matheus')
teste.append(70)
# print(teste)
galera = list()
galera.append(teste[:])
# print(galera)
teste[0] = 'jr duble'
teste[1] = 40
galera.append(teste[:])
galera[1][0] = 'Luiggi'
galera[1][1] = 2
# print(galera)

# for p in galera:
    # print(f'Nome: {p[0]}, Nº: {p[1]}')

print('-='*30)

dados = []
galera2 = []
for p in range(0, 2):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera2.append(dados[:])
    # dados.clear()

print(galera2)
# for p in galera2:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior')
#     else:
#         print(f'{p[0]} é menor')