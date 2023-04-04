# A confederacao nacional e natacao precisa de um programa que leia o ano de nascimento de um atleta e mostreu sua categoria
#de acordo com sua idade.
# Ate 9 anos : Mirim / Ate 14 anos: infantil  /  Ate 19 anos: Junior / ate 25 anos:  Senior / acima de 25: Master.

import datetime
ano = int(input('Qual seu ano de nascimento? '))
a = datetime.date.today()
a1 = (a.year - ano)
if a1 <= 9:
    print('Voce esta na categoria Mirim, pois voce tem {} anos'.format(a1))
elif a1 > 9 and a1 <= 14:
    print('Voce esta na categoria infantil, pois voce tem {} anos'.format(a1))
elif a1 > 14 and a1 <= 19:
    print('Voce esta na categoria Junior, pois voce tem {} anos '.format(a1))
elif a1 > 19 and a1 <=25:
    print('Voce testa na categoria Senior, pois voce tem {} anos '.format(a1))
else:
    print('Voce esta na categoria Master, pois voce tem {} anos'.format(a1))
