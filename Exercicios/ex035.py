# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo.

v1 = float(input('Diga  algum valor'))
v2 = float(input('Diga outro valor'))
v3 = float(input('Diga outro valor'))
if v1 < v2 + v3  and v2 < v1 + v3  and v3 < v1 + v2:
    print('Os valores acima podem formar um triangulo.')
else:
    print('Os valores nao podem formar um triangulo')