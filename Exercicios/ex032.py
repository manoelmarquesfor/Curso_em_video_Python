# Faca um programa que leia um ano qualquer e mostre se ele e bissexto


print('Vamos descobrir se o ano e bissexto?')
n = int(input('Diga um ano. ').strip())
t1 = n % 4
t2 = n % 400
t3 = n % 100

print(t1 , t2, t3 )
if (t1 == 0) and  (t3 != 0 ) or (t2 == 0):
    print('Bissexto')
else:
    print('Nao e')