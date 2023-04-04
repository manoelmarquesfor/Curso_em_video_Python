# Faca um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade:
# - Se ele ainda vai se alistar ao servico militar.
# - Se e a hora de se alistar.
# - Se ja passou do tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

import datetime

print('=-'*20)

ano = int(input('Em qual ano voce nasceu?  '))
a = datetime.date.today()
b = (a.year - ano)
#print(a.year - a )
#print(b)
if b < 18:
    print('Falta {} anos para se alistar'.format(18 - b))
elif b == 18:
    print('Voce precisa se alistar no servico militar')
elif b > 18:
    print('Voce ja passo da idade de se alistar.')
