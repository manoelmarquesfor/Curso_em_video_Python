#Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista unica que mantenha
#separado os valores pares e impares. No final mostre o valores pares e impares em ordem crescente.

numeros = [[],[]]

for n in range(1,8):
    temp = int(input(f'Digite o {n} valor: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)

numeros[0].sort()
print(f'Os numeros pares sao{numeros[0]}')
numeros[1].sort()
print(f'Os numeros impares sao{numeros[1]}')