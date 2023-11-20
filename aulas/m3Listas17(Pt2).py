# LISTAS PARTE 2

# LISTAS COMPOSTAS (Listas dentro de listas)
# adicionar estruturas compostas às Listas

dados = []
dados.append('Matheus')
dados.append(10)

pessoas = list()
# lembrar sempre de fazer uma cópia
pessoas.append(dados[:])
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
# print(galera)

print('-='*30)

