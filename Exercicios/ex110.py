# Adicione ao modulo moeda.py criado nos exercicios anteriores, uma funcao chamada resumo(), que mostre na tela algumas
# informacoes geradas pelas funcoes que ja temos no modulo criado ate aqui.

import moeda110

p = float(input('Digite o valor: '))
a = int(input('Aumentar quantos %: '))
d = int(input('Diminuir quantos %: '))
moeda110.resumo(p, a, d)