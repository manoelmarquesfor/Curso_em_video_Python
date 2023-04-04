# Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.

n = int(input('Diga um numero que vamos fazer sua tabuada de multiplicacao. '))

for c1 in range(1,11):
    print('{} x {} = {}'.format(n,c1,(n * c1)))