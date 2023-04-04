# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
#calcule e mostre o valor da hipotenusa

import math

co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hi = math.hypot(co,ca)

print('O valor de hipotenusa e igual a {}' .format(hi))