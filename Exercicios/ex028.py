# Escreva um programa que faca o computador pensar, em um numero inteiro de 0 a 5 e peca para o usuario tentar descobrir qual foi o
# numero escolhido pelo computador.  O prograva deverar escrever se o usuario venceu ou perder.
import random

a = random.randint(0,5)
b = int(input('Diga um numero de 0 a 5. ').strip())
if a == b:
    print('Voce venceu')
else:
    print('Voce perdeu, o numero correto era {}'.format(a))
