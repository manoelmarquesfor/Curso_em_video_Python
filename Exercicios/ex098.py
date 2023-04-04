# Faca um programa que tenha uma funcao chamada contador(), que recebe tres parametros: inicio, fim e passo e realize a contagem.
# Seu programa tem q realizar tres contagens atravez da funcao criada:
# a) De 1 ate 10, de 1 em 1
# b) De 10 ate 0, de 2 em 2
# c) uma contagem personalizada.

from time import sleep

def contagem(i, f, p):
    if p == 0:
        p = 1

        if i < f:
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f + 1, p):
                print(x, end=' ')
                sleep(0.5)
            print('Fim')

        elif p < 0 and i > f:
            p = p * -1
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f -1, -p):
                print(x, end=' ')
                sleep(0.5)
            print('Fim')

        elif i > f:
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f - 1, -p):
                print(x ,end=' ')
                sleep(0.5)
            print('Fim')
    else:
        if i < f:
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f + 1, p):
                print(x, end=' ')
                sleep(0.5)
            print('Fim')

        elif p < 0 and i > f:
            p = p * -1
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f - 1, -p):
                print(x, end=' ')
                sleep(0.5)
            print('Fim')

        elif i > f:
            print('=-' * 20)
            print(f'Contagem de {i} ate {f} de {p} em {p}')
            for x in range(i, f - 1, -p):
                print(x, end=' ')
                sleep(0.5)
            print('Fim')

contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-' * 20)
print('Agora e sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
