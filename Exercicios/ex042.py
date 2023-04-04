#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado.
# Equilatero: todos os lados iguais / Isosceles: dois lados iguais   /  escaleno: todos os lados diferentes


v1 = float(input('Diga  algum valor'))
v2 = float(input('Diga outro valor'))
v3 = float(input('Diga outro valor'))
if v1 < v2 + v3  and v2 < v1 + v3  and v3 < v1 + v2:
    print('Os valores acima podem formar um triangulo ', end='')
    if v1 == v2 == v3:
        print('Equilatero')
    elif v1 != v2 != v3 != v1:
        print('Escaleno')
    else:
         print('Isosceles')
else:
    print('Os valores nao podem formar um triangulo')