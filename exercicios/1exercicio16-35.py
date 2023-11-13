import math
import os
import pygame
import random
import calendar
from datetime import date

# pygame.init()

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 16. recebe um numero real pelo usuário e mostra sua porção inteira no console
def converterRealInteiro():
  numReal = float(input('Digite um nº real: '))
  print(f'A porção inteira é {math.trunc(numReal)}')
# converterRealInteiro();

# 17. Calcular o comprimento da hipotenusa
def calcularHipotenusa():
  catetoOposto = float(input('digite o comprimento oposto: '))
  catetoAdjacente = float(input('digite o comprimento adjacente: '))
  quadradoHipotenusa = catetoOposto **2 + catetoAdjacente**2
  comprimentoHipotenusa = math.sqrt(quadradoHipotenusa)
  print(f'O comprimento da hipotenusa: {comprimentoHipotenusa:.2f}')
# calcularHipotenusa()

# 18. Calcular seno, coseno e tangente de um ângulo
def calcAngulo():
  angulo = math.radians(30)
  seno = print(f'O seno de {angulo} é {math.sin(angulo):.2f}')
  coseno =  print(f'O coseno de {angulo} é {math.cos(angulo):.2f}')
  tangente = print(f'A tangente de {angulo} é {math.tan(angulo):.2f}')
# calcAngulo()

# 19. Sortear entre 4 alunos o escolhido para o quadro
def sorteioAlunos():
  alunos = ["Mat", "Lui", "Xan", "Tata"]
  numSorteado = random.randint(0, 3)
  for aluno in alunos:
    alunoSorteado = alunos[numSorteado]
  print(f'{alunoSorteado} foi escolhido pra se foder no quadro; parabéns!!!')
# sorteioAlunos()

#19.1 Sorteio 2
def sorteioAlunos2():
  lista = ["Mat", "Xan","Lui", "Tata"]
  escolhido = random.choice(lista)
  print(f'O escolhido foi {escolhido}')
# sorteioAlunos2()

# 20. Sortear a ordem de apresentação dos alunos anteriores
# não rolou
def sorteioOrdemApresentacao():
  alunos = ["Mat", "Lui", "Xan", "Tata"]
  ordemApresentacao = []
  while alunos > 0:
    for al in alunos:
      indexSort = random.randint(0, len(alunos) - 1)
      alunoSorteado = alunos[indexSort]
      ordemApresentacao.append(alunoSorteado)
      alunos.remove(alunoSorteado)
  print(ordemApresentacao)
# sorteioOrdemApresentacao()

# 20.1 Sorteio 2 - solução preguiçosa Guanabara
def sorteioOrdem2():
  alunos = ["Mat", "Lui", "Xan", "Tata"]
  # escolhidos = random.sample(alunos, k=2)
  random.shuffle(alunos)
  print(f'os escolhidos foram {alunos}')
# sorteioOrdem2()

# 21. Programa q abra e reproduza o áudio de um arquivo MP3 - usa lib pygame
def reproduzirMP3():
  pygame.mixer.music.load('nomedoarquivoOUPath')
  pygame.mixer.music.play()
  pygame.event.wait()
# reproduzirMP3()

# 22. ler o nome da pessoa e mostrar: 1)nome em maiusculo; 2)minusculo; 3)qntidade letras 4) qntas letras no primeiro nome
def stringManip():
  nome = input('Digite seu nome completo: ')
  print(nome.upper())
  print(nome.lower())
  print(len(nome) - nome.count(" "))
  primNome = nome.split()[0]
  print(primNome + "   |   " + str(len(primNome)) + " letras")
# stringManip()

# 23. ler nº de 0 a 9999 e mostrar na tela cada um dos dígitos separados
#tá errado...
def lerNumero():
  numero = input('Digite um nº entre 0 e 9999: ')
  print(f"unidade: {numero[0]}")
  print(f"dezena: {numero[1]}")
  print(f"centena: {numero[2]}")
  print(f"milhar: {numero[3]}")
# lerNumero()

# 24. ler cidade e verificar se ela começa com o nome santo
def comecaComSanto():
  cidade = input('digite o nome de uma cidade: ').strip()
  listCid = cidade.split(" ", -1)
  strCid = "".join(listCid)
  if strCid[0:5].upper() == "SANTO":
    print('vc é SANTO')
  else:
    print('NÃO tem SANTO')
# comecaComSanto()

# 25. Dizer se tem silva no nome
def temSilva():
  nome = input('digite seu nome: ').strip()
  encontrou = nome.lower().find("silva")
  if encontrou == -1:
    print('n tem silva')
  else:
    print('tem silva')
# temSilva()

# 26. ler uma frase e mostrar 1) qntas vezes aparece a letra A 2) em q posição aparece primeiro; 3) em q posição aparece por último
def encontrarLetraA():
  frase = input('escreva uma frase: ').strip().lower()
  vezesApareceu = frase.count('a')
  primeiroA = frase.find("a")
  ultimoA = frase.rfind("a")
  print(vezesApareceu)
  print(primeiroA)
  print(ultimoA)
# encontrarLetraA()

# 27. mostrar primeiro e último nome da pessoa
def primeiroUltimoNome():
  nome = input('digite seu nome completo: ');
  listNome = nome.split();
  primNome = listNome[0]
  ultNome = listNome[len(listNome) - 1]
  print(primNome)
  print(ultNome)
# primeiroUltimoNome()

# 28. usuário fala um número de 1 a 5, código gera aleatório. Verificar e se dizer se vencey
def guessingGame():
  rand = random.randint(1, 5)
  n = int(input('Digite um nº de 1 a 5: '))
  print(f'nº sorteado: {rand}')
  if rand == n:
    print('Parabéns, vc acertou!')
  else:
    print('Tente outra vez.')
# guessingGame()

# 29. > 80km = MULTA. 7 reais por cada km acima do limite
def multa():
  vCarro = int(input('A qntos km por hora vc estava andando?'))
  if vCarro > 80:
    vExcedida = vCarro - 80
    valorMulta = vExcedida * 7
    print(f'Vc será multado no valor de R$ {valorMulta:.2f}')
  else:
    print('Boa viagem!')
# multa()

# 30. par ou impar
def parOuImpar():
  n = int(input('Escreva um nº inteiro: '))
  if n % 2 == 0:
    print(f'{n} é par')
  else:
    print(f'{n} é ímpar')
# parOuImpar()

# 31. pergunta Distância em Km, calcula preço da passagem por 0,50 por km até 200km e 0,45 para viagens mais longas
def calcViagem():
  km = float(input('Qual a distancia da viagem? '))
  precoPassagem = 0
  if km <= 200:
    precoPassagem = km * 0.50
    print(f'o preço será de {precoPassagem:.2f}')
  else:
    precoPassagem = km * 0.45
    print(f'o preço será de {precoPassagem:.2f}')
# calcViagem()

# 32 Dizer se ano é bissexto
def anoBissexto():
  ano = int(input('Digite um ano (formato em 4 dígitos): '))
  if ano == 0:
    ano = date.today().year
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('é bissexto')
  else:
    print('não é bissexto')
  # if calendar.isleap(ano):
  #   print(f'{ano} é bissexto')
  # else:
  #   print(f"{ano} não é")
# anoBissexto()

# 33. mostrar maior e menor numero
def maiorMenor():
  n1 = int(input('Digite um nº: '))
  n2 = int(input('Digite um nº: '))
  n3 = int(input('Digite um nº: '))
  maior = n2
  if n1 > n2 and n1 > n3:
    maior = n1
  if n3 > n1 and n3 > n2:
    maior = n3
  menor = n2

  if n1 < n2 and n1 < n3:
    menor = n1
  if n3 < n1 and n3 < n2:
    menor = n3
  print(f'Maior: {maior}')
  print(f'Menor: {menor}')

  # largest = max(n1, n2, n3)
  # smallest = min(n1, n2, n3)
  # print(f'Maior: {largest}')
  # print(f'Menor: {smallest}')
# maiorMenor()

# 34. aumento salarial
def aumentoSalarial():
  salario = float(input('Qual o seu salario? '))
  aumento10 = salario * 0.10
  aumento15 = salario * 0.15
  if salario > 1250.00:
    print(f'Seu novo salário será de {salario + aumento10}')
  else:
    print(f'Seu novo salário será de {salario + aumento15}')
# aumentoSalarial()

# 35.  ler comprimento 3 retas e dizer se podem ou não formar um triângulo
def formarTriangulo():
  print('-='*20)
  print('Analisador de triangulos')
  print('-='*20)
  l1 = float(input('Informe o valor do lado 1: '))
  l2 = float(input('Informe o valor do lado 2: '))
  l3 = float(input('Informe o valor do lado 3: '))
  ladoMaior = max(l1, l2, l3)
  ladoMenor = min(l1, l2, l3)
  ladoMeio = l1
  if l2 > l1 and l2 < l3 or l2 > l3 and l2 < l1:
    ladoMeio = l2
  if l3 > l1 and l3 < l2 or l3 > l2 and l3 < l1:
    ladoMeio = l3
  if ladoMenor + ladoMeio > ladoMaior:
    print('forma triangulo')
  else:
    print('nao forma')
# formarTriangulo()