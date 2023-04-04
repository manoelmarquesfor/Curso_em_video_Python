# Faca um programa que calcule a soma entre todos os numeros impares que sao multiplo de tres e que se encontram no intervalo de 1 ate 500.
s= 0
cont = 0
for c in range(1 , 501 , 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados e {}' .format(cont, s))