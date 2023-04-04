#Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado
#e a quantidade de dias pelo qual foi alugado, Calcule o preco a pagar, sabendo que
#o carro custa R$ 60 por dia e RS 0.15 por km rodado

print('='*7,'Vamos calcular o aluguel do carro', '='*7)
dias = int(input('Quantos dias o carro ficou com você? '))
km = float(input('Quantos km o carro percorreu? '))
v= (dias*60)+(km*0.15)
print('O carro percorreu {}km e ficou {} dias com você, entao tera que pagar o valor de R$ {}{:.2f}{}.' .format(km, dias,'\033[1;31m',v,'\033[m'))