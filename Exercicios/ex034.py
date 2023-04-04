# escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.
# Para salario superiores a  R$ 1250,00 calcule um valor de 10%
# Para os inferiores ou iguais o aumento e de 15%

s = float(input('Qual seu salario? '))
if s <= 1250:
    print('Seu novo salario e {}' .format(s+(s/100*15)))
else:
    print('Seu novo salario e {}'.format(s+(s/100*10)))