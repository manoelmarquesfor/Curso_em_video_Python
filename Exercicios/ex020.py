# O mesmo professor do exercicio anterior quer sortear a ordem de apresentacao de trabalho de alunos. Faca um
#programa que leia o nome dos quatro alunos e mostre a ordem sorteada


import random

a = input('Diga um nome')
b = input('Diga outro nome')
c = input('Diga mais um nome')
lista = [a,b,c]
r = random.shuffle(lista)

print('A sequencia escolhida e.' )
print(lista)