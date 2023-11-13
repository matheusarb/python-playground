import os
os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# Printar olá mundo
def hw():
  p = print('olá, mundo')
  p;
# hw();

# Saudar usuário
def saudacao():
  nome = input('Digite o seu nome: ');
  print(f'Olá, {nome}, muito prazer!');
# saudacao();

# Soma
def soma():
  n1 = int(input('digite o primeiro nº: '));
  n2 = int(input('digite o segundo nº: '));
  s = n1 + n2;
  print('O valor da soma de {0} + {1} é {2}'.format(n1, n2, s));
  print(f'O valor da soma de {n1} + {n2} = {n1+n2}')
# soma();

# 1. ler um nº inteiro e mostrar na tela seu antecessor e sucessor
def exerc1():
  n = int(input('escreva um nº: \n'));
  print(f'o antecessor de {n} é {n - 1} e o seu sucessor é {n + 1}')
# exec1();

# 2. IMPORTANTE(Sintaxe pra calcular RAIZ QUADRADA) Printar na tela o dobro, triplo e raiz quadrada de um nº
def exerc2():
  n = int(input('digite um nº '));
  print(f'o dobro de {n} é {n*2}')
  print(f'o triplo de {n} é {n*3}')
  print(f'a raiz quadrada de {n} é {n ** (1/2):.2f}')
  print(f'a raiz quadrada de {n} é {pow(n, (1/2)):.2f}')
# exerc2()

# 3.

# 4. Leia um input do usuário e mostre na tela o tipo primitivo e todas as infos possíveis sobre o dado
def exerc4():
  inp = input('Digite alguma coisa: ')
  print('É alfanumérico?', inp.isalnum());
  print('É um decimal?', inp.isdecimal());
  print('E um animal, ele é?', inp.isdecimal());
  print('Está em maiúscula?', inp.isupper());
# exerc4();

# CALCULAR A RAIZ QUADRADA DE UM Nº É A MESMA COISA QUE CALCULAR  A POTÊNCIA DELE POR MEIO (1/2)
def raizQuadrada(num):
  print(f'{num**(1/2)}')
# raizQuadrada(2890238902)

# RAIZ CÚBICA É A POTÊNCIA DO Nº A UM TERÇO 1/3
def raizCubica(num):
  print(f'{num ** (1/3)}')
# raizCubica(92)

# 8. Ler valor em metros e exibir convertido em centimetros e milimetros
def converterMetros():
  inp = float(input('Digite a metragem: '));
  cm = inp * 100
  mm = inp * 1000
  print(f'A metragem {inp}m em centímetros é: {cm:.0f}cm e milímetros é: {mm:.0f}mm');
# converterMetros();

# 9. Tabuada de um nº
def tabuada(num):
  i = 1;
  print('-'*10)
  while i <= 10:
    result = num * i;
    print(f'{num} x {i} = {result}');
    i = i + 1;
# tabuada(5)

# 10. Programa que leia qnto dinheiro existe na carteira e quantos dólares ela pode comprar
def comprarDolar(real):
  dolar = real / 3.27
  print(f'Eu tenho {real} reais. Posso comprar {dolar:.2f} dólares')
# comprarDolar(30.32)

# 11. Programa pra ler a largura e a altura de uma parede em metros,
# calcular a sua área e a quantidade de tinta necessária para pintá-la
# a cada 2m² eu usarei 1L de tinta
# área = base x altura
def calcAreaTinta(largura, altura):
  area = float(largura*altura);
  tinta = area / 2; #1l de tinta pra cara 2m. ENtão, divido por dois
  print(f'A área total da parede é de {area:.2f}. A quantidade de tinta será de {tinta:.2f}')
# calcAreaTinta(5.75, 5.12)

# 12. Desconto de 5% no produto
def descontoProduto(preco):
  desconto = preco * 0.05;
  print(f'O produto custa {preco:.2f} reais mas sairá por {preco - desconto:.2f}')
# descontoProduto(927.23)

# 13. Salário do funcionário com 15% de aumento
def aumentoSalarial(salario):
  aumento = 1.15;
  aumento2 = 115/100;
  salarioFinal = salario * aumento
  print(f'Seu salário hoje é de {salario:.2f}. Aumentado 15% ficará {salarioFinal:.2f}')
# aumentoSalarial(10000)

# 14. Conversão de temperatura de celsius pra farenheit
def conversorTemperatura(celsius):
  farenheit = celsius * 1.8 + 32;
  print(f'A temperatura em celsius é {celsius}ºC, e em farenheit é {farenheit}ºF')
# conversorTemperatura(31.5)

# 15. Aluguel de carros
def AlugarCarro():
  diasAlugado = int(input('Por quantos dias você rodou com ele? '))
  kmRodados = float(input('Quantos km o carro percorreu? '))
  valorAluguelCarro = (diasAlugado * 60) + (kmRodados * 0.15)
  print(f'O valor do aluguel é de {valorAluguelCarro:.2f}')
# AlugarCarro();