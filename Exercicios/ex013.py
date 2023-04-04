# Faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

s = float(input('Qual seu salario? '))
n= s + (15/100*s)
print('Seu novo salario e {} R$'.format(n))