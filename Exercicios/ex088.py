# Faca um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
# perguntar quantos jogos serao gerador e vai sortear 6 numeros entre 1 e 60 para cada
# jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

lista = []
jogos = []
print('-'*42)
print(f'               Jogo Mega Sena         ')
print('-'*42)
pergunta = int(input('Quantos jogos voce quer que eu sorteie? '))

tot = 1
while tot <=pergunta:
    cont = 0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-='*5 ,f'Sorteando {pergunta} jogos','-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo{i+1}:{l}')
    sleep(1)
print('-='*7 ,f'Boa Sorte','-='*7)