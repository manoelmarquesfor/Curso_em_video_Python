# Faca um programa que leia tres numeros e mostre qual e o maior e qual o menor.

n1 =  int(input('Diga um numeros').strip())
n2 =  int(input('Diga um numeros').strip())
n3 =  int(input('Diga um numeros').strip())

maior = n1
if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3
print('O maior valor  e', maior)
