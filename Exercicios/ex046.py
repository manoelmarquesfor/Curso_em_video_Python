#Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
#indo de 10 ate 0, com uma pausa de 1 segundo entre elas.

import time
import emoji

print('Contagem regressiva para queima de fogos')

for c in range(11 , 0, -1):
    print(c)
    time.sleep(0.5)
print(emoji.emojize(':boom: BOUMMMM :boom:', use_aliases=True ))