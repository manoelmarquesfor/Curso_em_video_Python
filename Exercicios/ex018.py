# Faca um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse agulo


import math
a = float(input('Qual o angulo que vc quer calcular? '))
r = math.radians(a)
seno = math.sin(r)
cos =  math.cos(r)
tan =  math.tan(r)

print('O angulo de {} e  seno e {:.2f}'.format(a,seno))
print('O angulo de {} e  cosseno e {:.2f}'.format(a, cos))
print('O angulo de {} e tangente e {:.2f}'.format(a, tan))
