#Faca um algoritimo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto

p = float(input('Qual o preco do produto? '))
d = p - (5/100*p)

print('O produto tem o valor normal de {} R$ e com desconto o valor fica {} R$.'.format(p, d) )