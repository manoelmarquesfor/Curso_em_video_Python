# Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiro termos da progressao usando estrutura while.

p = int(input('Primeiro termo: '))
r = int(input('Razao '))
termo = p
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo = termo + r
    cont = cont + 1
print('Fim')
