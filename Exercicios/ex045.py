# Crie um programa que que faca o computador jogar Jokenpô  com voce.

import random

lista = ['PEDRA','PAPEL', 'TESOURA']
pc = random.randint(0 , 2)
print('''Suas opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jg = int(input('Qual sua jogada?'))
print('=-'*20)
print('Computador jogou {}.'.format(lista [pc] ))
print('Jogador jogou {}'.format(lista[jg]))
print('=-'*20)

if pc == 0:
    if jg == 0:
        print('EMPATE')
    elif jg == 1:
        print('Jogador Venceu')
    elif jg == 2:
        print('Computador Venceu')
    else:
        print('Jogada invalida')

elif pc == 1:
    if jg == 0:
        print('Computador venceu')
    elif jg == 1:
        print('EMPATE')
    elif jg == 2:
        print('Jogador venceu')
    else:
        print('Jogada invalida')

elif pc == 2:
    if jg == 0:
        print('Jogador venceu')
    elif jg == 1:
        print('Computador Venceu')
    elif jg == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')