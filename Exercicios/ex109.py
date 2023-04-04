# Modifique as funcoes que foram criadas no ex107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai,
# ser ou nao formatado pela funcao moeda(), desenvolvida no ex108

import moeda2


p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.metade(p, True)}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.dobro(p, True)}')
print(f'Aumentado 10% de {moeda2.moeda(p)} é {moeda2.aumento(p, 10, True)}')
print(f'Reduzindo 30% de {moeda2.moeda(p)} é {moeda2.diminuir(p, 30, True)}')