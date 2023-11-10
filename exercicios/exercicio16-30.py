import math
import os
import random
import pygame

pygame.init()

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
sorteioOrdem2()

# 21. Programa q abra e reproduza o áudio de um arquivo MP3 - usa lib pygame
def reproduzirMP3():
  pygame.mixer.music.load('nomedoarquivoOUPath')
  pygame.mixer.music.play()
  pygame.event.wait()
# reproduzirMP3()