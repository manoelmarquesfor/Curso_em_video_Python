#Desenvolva um programa que leia as 2 notas de um aluno e tire sua media.

nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
r = (nota1 + nota2) / 2
print('A media do aluno e {:.1f}' .format(r))