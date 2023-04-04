# Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatacao correta.

'''
matriz = [[],[],[]]

for n in range(0,3):
    n=int(input(f'Digite um valor para [0,{n}]'))
    matriz[0].append(n)

for n in range(0,3):
    n=int(input(f'Digite um valor para [1,{n}]'))
    matriz[1].append(n)

for n in range(0,3):
    n=int(input(f'Digite um valor para [2,{n}]'))
    matriz[2].append(n)


print('=-'*5, 'RESULTADO DA MATRIZ', '=-'*5)

print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')

'''

matriz = [[0,0,0,],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Diga um valor para [{l},{c}]'))
print('=-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
