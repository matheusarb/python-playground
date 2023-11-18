# TUPLAS
# 1. Tuplas são IMUTÁVEIS
# 2.

lanche = ('hamb', 'cerveja', 'pizza')
print('\033[4;31m-\033[m', lanche[1])
print('\033[4;31m-\033[m', lanche[1:])
print('\033[4;31m-\033[m', lanche[:2])
print('\033[4;31m-\033[m', len(lanche))
print('\033[4;31m-\033[m', type(lanche))


for c in lanche:
    print(c)

for count in range(0, len(lanche)):
    print(lanche[count])

