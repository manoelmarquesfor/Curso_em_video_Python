# Faca um programa que leia um numero de 0 a 9999 e mostre na tela a cada um dos digitos separados.
#ex: 8541     Unidade = 1  , dezena = 4 , centena = 5 , milhar = 8

n = int(input('Digite um numero. '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O numero digitado foi {}'.format(n))
print('Sua unidade e {}'.format(u))
print('Sua dezena e {}'.format(d))
print('Sua centena e {}'.format(c))
print('Sua milhar e {}'.format(m))

#print(n.)


