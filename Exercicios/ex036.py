# Escreve um programa para aprovar o emprestimo bancario para compra de uma casa. O programa vai perguntar
# o valor da casa , o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.


print('-'*10,'Calculo emprestimo', '-'*10)

valor = float(input('Qual o valor da casa ? '))
salario = float(input('Qual o valor do seu salario? '))
anos = int(input('Em quantos anos gostaria de pagar? '))
prestacao = valor / (anos * 12 )
if prestacao < (salario * 30 /100):
    print('Parabens, seu financiamento foi aprovado, o valor da prestacao sera {:.2f} e sera paga em {} meses.'.format(prestacao,(anos*12)))
else:
    print('Infelizmente seu emprestimo foi negado pois o valor da prestacao {:.2f} e maior que o valor so seu salario.'.format(prestacao))