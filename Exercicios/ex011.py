# Faca um programa que leia a altura e largura de uma parede em metros, calcule sua area e a quantidade
# de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²


altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

a = altura * largura
l = a / 2

print('Voce tem {:.3f}m² de area e precisa de {:.2f} litros de tinta para pintar toda essa parede3.' .format(a,l))