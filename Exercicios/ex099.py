# Faca um programa que tenha uma funcao chamada maior(), que receba varios parametros com valores inteiros.
# Seu programa tem q analisar todos os valores e dizer qual deles e o maior.

from time import sleep

def maior(* n):
    print('-='*30)
    print(f'Analisando os valores passados...')
    for x in n:
        print(x, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n)}')


maior(3,6,7,8,9,10)
maior(5,6,7)
maior(10,264567,15)
