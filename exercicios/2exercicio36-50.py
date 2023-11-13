import datetime
import math
import os
import random
import calendar

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 36. aprovar empréstimo com base no valor da casa, salário e anos para quitar
def emprestimoBancario():
    valCasa = float(input('Qual o valor da casa? '))
    valSalario = float(input('Qual o seu salário? '))
    prazoQuitacao = float(input('Em quantos anos será quitada? ')) * 12
    prestacaoMensal = valCasa / prazoQuitacao
    limiteSalario = valSalario * 0.30
    if prestacaoMensal <= limiteSalario:
        print(f'* Seu salário: {valSalario:.2f}\n* Limite do salário para a prestação: {limiteSalario:.2f}\n* Valor da prestação ({prestacaoMensal:.2f})')
        print('Empréstimo concedido')
    else:
        print(f'O valor da prestação ({prestacaoMensal:.2f}) excede o limite permitido (até 30% do salário: {limiteSalario:.2f}).')
# emprestimoBancario()

# 37. ler um inteiro e perguntar qual será a base de conversão (binário, octal, hexadecimal)
# não rolou e n entendi
def converterInteiro():
    num = int(input('Digite um nº inteiro: '))
    conversor = int(input('Escolha um dígito para o método de conversão:\n1. Binário\t2. octal\t3. hexadecimal '))

    if conversor == 1:
        def convBin(num):
            result_binario = ""
            while num > 0:
                resto = num % 2
                result_binario = str(resto) + result_binario
                num //= 2
            print(result_binario)
        convBin(num)
# converterInteiro()

# 38. comparar 2 numeros inteiros
def compararNumeros():
    num1 = int(input('escreva um nº: '))
    num2 = int(input('escreva outro nº: '))
    if num1 > num2:
        print(f'{num1} é maior q {num2}')
    elif num2 > num1:
        print(f'{num2} é maior q {num1}')
    else:
        print('Os dois nºs são iguais')
# compararNumeros()

# 39. data de alistamento
def alistamentoMilitar(anoNasc):
    periodoParaAlistamento = anoNasc + 18
    anoAtual = datetime.date.today().year
    if periodoParaAlistamento < anoAtual:
        print(f'O período para alistamento prescreveu há {anoAtual - periodoParaAlistamento} anos. Vc deveria ter ido em {periodoParaAlistamento}')
    elif periodoParaAlistamento > anoAtual:
        print(f'Ainda não chegou a sua vez, faltam {abs(anoAtual - periodoParaAlistamento)} anos. Vc deverá comparecer em {periodoParaAlistamento}')
    else:
        print(f'Vá para a unidade mais próximo para alistamento. Seu período ({periodoParaAlistamento}) chegou.')
# alistamentoMilitar(2010)

# 40.