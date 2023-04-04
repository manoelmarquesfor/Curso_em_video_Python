# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

from datetime import date

atual = date.today().year
totMaior = 0
totMenor = 0

for n in range(1,8):
    nasc = int(input('Em qual ano a {} pessoa nasceu? '.format(n)))
    idade = atual - nasc
    if idade >= 21:
        totMaior = totMaior + 1
    else:
        totMenor = totMenor + 1
print('Ao todo tivemos {} pessoa maiores de idade' .format(totMaior))
print('E tambem tivemos {} pessoas menores de idade' .format(totMenor))
