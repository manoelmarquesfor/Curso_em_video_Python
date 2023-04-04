# Adapte o codigo do ex107, criando uma funcao adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.

import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Reduzindo 30% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 30))}')