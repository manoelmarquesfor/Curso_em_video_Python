# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar 7R$ por cada km acima do limite.

import emoji
import time

print('-='*20)

velocidade = float(input('Qual a valocidade do carro? '))
multa = (velocidade-80) * 7
print('Analizando!!!')
time.sleep(2)
if velocidade < 81:
    print('Parabens, voce nao foi multado')
else:
    print(emoji.emojize('Voce foi multado em {}{}{} R$ :fu:',use_aliases=True) .format('\033[1;31m',multa,'\033[m'))
    print(emoji.emojize('Pau no :ok_hand: do :cat:',use_aliases=True))
print('-='*20)

