# LISTAS
lista = ['banana', 'maçã', 'limão']

#ADICIONAR
# add elementos ao final da lista
lista.append('cookie')
print(lista)

# add elemento em posição determinada
lista.insert(0, 'sorvete')
lista.insert(2, 'uva')
print(lista)

#APAGAR
del(lista[1])
print(lista)
lista.pop(-2)
print(lista)
if 'tutu' in lista:
    lista.remove('tutu')
else:
    print('tutu n está na lista')
# lista.remove('tutu')
print(lista)

#CRIAR lista
valores = list(range(3, 7))
print(valores)

#ORDENAR lista
# sort retorna None
lista2 = [8, 2, 5, 12, 7]
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
print('-='*20)

#FORMAS DE LOOP NA LISTA LEMBRAR DISSO AQUI
for n in lista2:
    print(n, end=' ')
print()

for pos, n in enumerate(lista2):
    print(f'na pos {pos} o valor é {n}')

print('-='*20)
# n1=1
length = len(lista2)-1
for n1 in range(0, length):
    print(f'na pos {n1} o valor é {lista2[n1]}')
print(len(lista2))