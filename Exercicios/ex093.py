# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cadas partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou: '))
for x in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {g} ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas')
for n in range(0, len(gols)):
    print(f'    => Na partida {n}, fez {gols[n]} gols')
print('-='*20)
print(f'Foi um total de {jogador["total"]} gols ')