#Crie um programa que leia quanto de dinheiro uma pessoa
# tem na carteira e mostre quantos dolares ela pode comprar.
# Considere USS 1.00 = R$ 3.27
print('Vamos fazer um conversor de REAL para Dolar')
n1 = float(input('Quantos reais você tem? '))
d= n1 / 3.27
print('Voce tem {} reais que convertendo vai ser {}{:.2f}{} dolares' .format(n1,'\033[32m',d,'\033[m'))