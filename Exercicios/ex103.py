# Faca um programa que tenha uma funcao chamada ficha(), que receba 2 parametros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.


def ficha(nome = '<desconhecido>', gols = 0):
    return f'O jogador {nome} fez {gols} no campeonato'


n = str(input('Nome do jogador: '))
g = str(input('Quantos gols marcou: '))

if n.strip() == '':
    n = '<desconhecido>'
else:
    ficha(n)
if g.isnumeric():
    g = int(g)
else:
    g = 0

print(ficha(n, g))