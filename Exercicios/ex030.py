# Crie um programa que leia um numero inteiro e mostre na tela se ele e impar ou par.

n = int(input('Digite um numero. ').strip())
v = n % 2
cor = {'azul':'\033[34m','vermelho':'\033[31m', 'nada':'\033[m'}
if v == 0:
    print('O numero e {}par{}'.format(cor['azul'], cor['nada']))
else:
    print('O numero e {}impar{}'.format(cor['vermelho'],cor['nada']))

