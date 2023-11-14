import datetime
import math
import os
import random
import calendar
import sys
import time

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# 36. aprovar empréstimo com base no valor da casa, salário e anos para quitar
def emprestimoBancario():
    valCasa = float(input('Qual o valor da casa? R$'))
    valSalario = float(input('Qual o seu salário? R$'))
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

    if conversor != 1 and conversor != 2 and conversor != 3:
        print('Método de conversão inválido! Tente novamente')
        time.sleep(1.0)
        converterInteiro()

    if conversor == 1:
        print(f'O nº convertido para binário é {bin(num)}')
    elif conversor == 2:
        print(f'O nº convertido para octal é {oct(num)[2:]}')
    else:
        print(f'O nº convertido para hexadecimal é {hex(num)}')
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

# 40. média de aluno
def mediaEscolar(n1: float, n2: float) -> print():
    media = float((n1 + n2) / 2)
    if media < 5:
        print('reprovado')
    elif 5 <= media <= 6.9:
        print('recuperação')
    else:
        print('aprovado')
# mediaEscolar(3.5, 5.5)
# mediaEscolar(6.5, 6)
# mediaEscolar(8.5, 9.5)

# 41. ano de nascimento do nadador e determinar categoria
def categoriaNadador(anoNasc: int):
    anoAtual = datetime.date.today().year
    idadeNadador = anoAtual - anoNasc
    if idadeNadador <= 9:
        print('mirim')
    elif 9 < idadeNadador <= 14:
        print('infantil')
    elif 14 < idadeNadador <= 19:
        print('junior')
    elif idadeNadador == 20:
        print('senior')
    else:
        print('Master')
# categoriaNadador(2014)
# categoriaNadador(2009)
# categoriaNadador(2004)
# categoriaNadador(2003)
# categoriaNadador(2000)

# 42. Foi para refazer o dos triângulos (desafio 35)

# 43. calcular imc
def calcularImc(peso: float, altura: float):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print('abaixo do peso')
    elif 18.5 <= imc <= 25:
        print('ideal')
    elif 25 < imc <= 30:
        print('sobrepeso')
    elif 30 < imc <= 40:
        print('obesidade')
    else:
        print('obesidade mórbida')
# calcularImc(45, 1.68)
# calcularImc(70, 1.68)
# calcularImc(82, 1.68)
# calcularImc(90, 1.68)
# calcularImc(120, 1.68)

# 44. calcular valor a ser pago pelo produto, considerando o preço e a FORMA DE PAGAMENTO
def calcularProduto(preco: float):
    formaPagamento = int(input('qual a forma de pagamento?\n1- à vista no dinheiro/cheque\n2- à vista no cartão\n3- em até 2x no cartão\n4- em até 3x ou mais no cartão'))
    descontoDinheiroCheque = preco * 0.10
    descontoCartao = preco * 0.05
    jurosParceladoTres = preco * 0.20

    if formaPagamento == 1:
        print(f'produto sairá por {preco - descontoDinheiroCheque}')
    elif formaPagamento == 2:
        print(f'produto sairá por {preco - descontoCartao}')
    elif formaPagamento == 4:
        print(f'produto sairá por {preco + jurosParceladoTres}')
    else:
        print(f'produto sairá por {preco}')
# calcularProduto(100)
# calcularProduto(100)
# calcularProduto(100)
# calcularProduto(100)

# 45. programa pra jogar jokenpô (...)
def jokenpo():
    escolhaUsuario = int(input('''Qual sua opção?
    [0] Pedra
    [1] Papel
    [2] Tesoura
    [3] Sair do programa
    : '''))
    if escolhaUsuario == 3:
        print('o jogo foi divertido! Até mais.')
        time.sleep(1)
        sys.exit()

    escolhaMaquina = random.randint(0,2)
    print('JO')
    time.sleep(0.2)
    print('KEN')
    time.sleep(0.3)
    print('PÔ!')
    time.sleep(0.3)

    if escolhaUsuario == 0:
        if escolhaMaquina == 0:
            print('Deu empate')
        elif escolhaMaquina == 1:
            print('Vc perdeu! Papel ganha de pedra')
        else:
            print('Você ganhou! Pedra ganha de Tesoura')

    if escolhaUsuario == 1:
        if escolhaMaquina == 0:
            print('Você ganhou! Papel ganha de Pedra')
        elif escolhaMaquina == 1:
            print('Deu empate')
        else:
            print('Você perdeu! Tesoura ganha de papel')

    if escolhaUsuario == 2:
        if escolhaMaquina == 0:
            print('Você Perdeu! Pedra ganha de Tesoura')
        elif escolhaMaquina == 1:
            print('vc ganhou! Tesoura ganha de papel')
        else:
            print('Deu empate')

    time.sleep(1.5)
    jokenpo()
# jokenpo()