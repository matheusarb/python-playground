# Condições aninhadas
nome = input('qual seu nome?').lower()
if nome == 'matheus' or nome == 'luiggi':
    print('vc é foda')
elif nome == 'xan' or nome == 'jota':
    print('vc tb é foda')
elif nome in 'milena, julia, vanessa':
    print('futura mãe de meus filhos')
else:
    print('vc é normal')