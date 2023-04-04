# Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faca um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido


import random

a = input('Diga um nome ')
b = input('Diga outro nome ')
c = input('Diga mais outro nome ')
lista = [a,b,c]
valores = random.choice (lista)
print('O escolhido e {}' .format(valores))