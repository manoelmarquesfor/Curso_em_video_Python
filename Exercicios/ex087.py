#Aprimore o exercicio anterior, mostrando no final
# a)A soma de todos os valores pares digitados.
# b)A soma dos valores da terceira coluna.
# c)O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Diga um numero para [{l},{c}]'))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par = soma_par + matriz[l][c]
    print()
print('--'*12)
print(f'A soma dos numeros pares e {soma_par}')
print(f'A soma dos valores da terceira coluna e {(matriz[0][2])+((matriz[1][2]))+((matriz[2][2]))}')
print(f'O maior valor da terceira coluna e {max(matriz[1])}')