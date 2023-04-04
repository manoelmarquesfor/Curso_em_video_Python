# Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de vizualizacao
# de detalhamento aproveitamento de cada jogador.


jogador = {}
jogadores = []
gols = []
print('-'*35)
c = -1
c1 = -1

while True:
    while True:
        jogador['nome'] = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {jogador["nome"]} ganhou: '))
        for x in range(0, partidas):
            gols_validado = str(input(f'Quantos gols na partida{x} ')).strip()
            if gols_validado in '':
                gols_validado= int(0)
            elif gols_validado.isalpha():
                print('Voce nao digitou um numero valido')
                gols_validado = str(input(f'Quantos gols na partida{x} ')).strip()
                gols_validado= int(gols_validado)
            else:
                gols_validado= int(gols_validado)
            gols.append(gols_validado)

        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
        jogadores.append(jogador.copy())
        jogador.clear()
        gols.clear()

        while True:
            pergunta = str(input('Deseja continuar? [S/N] ')).upper()[0]
            if pergunta in 'SN':
                break
            print('ERRO! Responda apenas S ou N. ')
        if pergunta == 'N':
            break
    if pergunta == 'N':
       break
print('-'*35)
print('  Cod  Nome         gols            total')

for k, v in enumerate(jogadores):
    print(f'{k:>4}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-'*35)
while True:
    p2= int(input('Mostrar dados de qual jogador: (999 para parar) '))
    if p2 == 999:
        break
    elif p2 >= len(jogadores):
        print(f'ERRO! Nao existe jogador com codigo {p2}! Tente Novamente')
    else:
        print(f' -- Levanamento do jogador {jogadores[p2]["nome"]} :')
        for x in jogadores[p2]['gols']:
            c1 = c1 + 1
            print(f'    No jogo {c1} fez {x} gols')
    print('-' * 35)
print('<< Volte Sempre >>')