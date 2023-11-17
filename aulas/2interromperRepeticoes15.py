# Interromper laços

# keyword break
soma = n = 0
while True:
    n = int(input('digite um nº: '))
    if n == 999:
        break
    soma += n
print(f'a soma deu {soma}')