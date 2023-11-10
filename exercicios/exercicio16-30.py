import math
import os
import random
import pygame

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
encontrarLetraA()

# 27. mostrar primeiro e último nome da pessoa
def primeiroUltimoNome():
  nome = input('digite seu nome completo: ');
  listNome = nome.split();
  primNome = listNome[0]
  ultNome = listNome[len(listNome) - 1]
  print(primNome)
  print(ultNome)
# primeiroUltimoNome()

