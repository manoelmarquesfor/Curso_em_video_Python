# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario.
# No final coloque esse dicionario em ordem, sabendo que o vancedor tirou o maior numero dado.


from random import randint
from time import sleep
dado = {}
c = 0
print('-='*15)
print('     Valores sorteados')
print('-='*15)

for n in range(1,5):
    dado[f'jogador{n}'] = randint(1 , 6 )

for x in dado.keys():
    print(f'O {x} tirou {dado[x]} no dado')
    sleep(0.5)
print('-='*15)
print('     Ranking dos jogadores')
print('-='*15)
sleep(0.5)

for v in sorted(dado, key=dado.get, reverse=True):
    c = c + 1
    print(f'{c}° lugar {v} com {dado[v]}')
    sleep(1)
