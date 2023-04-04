# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior que estao na tupla.
import random
from random import randint

numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(f'Os numeros sorteador foram ',end='')

for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor e {max(numeros)} e o menor numero e {min(numeros)}')

