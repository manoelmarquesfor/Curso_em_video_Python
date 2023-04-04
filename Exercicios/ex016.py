# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela somente sua porcao inteira


import math

n = float(input('Digite qualquer numero real '))
valor = math.trunc(n)

print('Seu numero inteiro e {}' .format(valor))