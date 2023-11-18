# TUPLAS
# 1. Tuplas são IMUTÁVEIS
# 2. Tuplas aceitam TIPOS DE DADOS DIFERENTES
# 3. NÃO podemos deletar um item específico dentro da Tupla através do del()

lanche = ('hamb', 'cerveja', 'pizza')
print('\033[4;31m-\033[m', lanche[1])
print('\033[4;31m-\033[m', lanche[1:])
print('\033[4;31m-\033[m', lanche[:2])
print('\033[4;31m-\033[m', len(lanche))
print('\033[4;31m-\033[m', type(lanche))

# parente do foreach
for c in lanche:
    print(f'Vou comer {c}')

# técnica adicional transformando em ENUMERATOR
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

for count in range(0, len(lanche)):
    print(f'Vou comer {lanche[count]} na posição {count}')

# sorted
print(sorted(lanche))
print(type(sorted(lanche)))

print('')
print('='*30)
print('')

a = (8, 7, 1)
b = (2, 3, 4)
c = a + b
print(len(c))
print(c.count(7))
print(c)
print(c.index(3))
del(b)
print(c)