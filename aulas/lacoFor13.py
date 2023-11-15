# Laço for
c=6
for c in range(0, c+1, 2):
    print(c)
print('Fim.')
if primo % c == 0:
    print(f'\033[33m', end='')
    totDivisivel += 1
else:
    print(f'\033[31m', end='')
print(f'{c} ', end=' ')
