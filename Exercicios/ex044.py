# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
# a vista dinheiro ou cheque: 10% de desconto
# a vista no cartao:5% de deconto
# em ate 2x cartao: preco normal
# 3x ou mais no cartao: 20% de juros


preco = float(input('Qual o valor do produto?  '))
print('''Condicoes de pagamento:
[1] Avista dinheiro ou cheque
[2] Avista no cartao 
[3] 2x no cartao 
[4] 3x ou mais no cartao''')
condicao = int(input('Qual a forma de pagamento?  '))
a = preco - (preco *10 /100 )
b = preco - (preco *5 /100 )
c = preco
d = preco + (preco *20 /100 )
if condicao == 1:
    print('Voce vai pagar {}'.format(a))
elif condicao == 2:
    print('Voce vai pagar {}'.format(b))
elif condicao == 3:
    print('Voce vai pagar {}'.format(c))
elif condicao == 4:
    print('Voce vai pagar {}'.format(d))