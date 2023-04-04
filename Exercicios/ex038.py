# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor e maior ,  o segundo valor e maior,  nao existe valor maior os dois sao iguais

import time

n1 = int(input('Diga um numero. '))
n2 = int(input('Diga outro numero. '))
print('Agora vamos comparar.')
print('Analizando !!!')
time.sleep(1)
if n1 > n2:
    print('O valor {} e maior que {}.'.format(n1,n2))
elif n2 > n1:
    print('O valor {} e maior que {}.'.format(n2, n1))
elif n1 == n2:
    print('Os valores, {} e {} sao iguais.'.format(n1,n2))