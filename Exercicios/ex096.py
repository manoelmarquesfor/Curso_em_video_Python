# Faca um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno retangular{largura e comprimento} e mostre a area do terreno.

def area(l , c):
    resultado = l*c
    print(f'A area do terreno {l} x {c} e de {resultado}m².')


print('Controle de terreno')
print('-'*20)
l = float(input('Largura: (m) '))
c = float(input('Comprimento: (m) '))
area(l , c)