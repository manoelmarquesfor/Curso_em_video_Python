#Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

n = int(input('Diga um numero. '))
tot = 0
for c in range(1 , n + 1):
    if n % c ==0:
        print('\033[33m', end='')
        tot = tot +1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\33[m O numero {} foi divisivel {} vezes '.format(n,tot))
if tot==2:
    print('E por isso ele e PRIMO')
else:
    print('E por isso ele NAO E PRIMO')