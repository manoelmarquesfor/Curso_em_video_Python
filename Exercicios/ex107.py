# Crie um modulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminui(), dobrar() e metade().
# Faca tambem um programa que importe esses modulos e use algumas dessas funcoes.

import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentado 10% de R$ {p} é R$ {moeda.aumento(p, 10)}')
print(f'Reduzindo 30% de R$ {p} é R$ {moeda.diminuir(p, 30)}')