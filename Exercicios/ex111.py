# Crie um pacote chamado utilidadeCeV que tenha dois modulos internos chamados moeda e dado.
# Transfira todas as funcoes utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


from utilidadesCev import moeda


p = float(input('Digite o valor: '))
a = int(input('Aumentar quantos %: '))
d = int(input('Diminuir quantos %: '))
moeda.resumo(p, a, d)