#Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um nuero entre 0 e 10. so que agora o jogador vai tentar
#adivinhar ate acertar. mostrando no final quantos palpites foram necessaios.

from random import randint

print('*'*10, 'Jogo do adivinha', '*'*10)
pc = randint(0 , 10)
jg = int(input('Diga um numero de 0 a 10 '))
c = 1
while jg != pc:
        if jg > pc:
            jg = int(input('\033[31m Errou \033[m, o numero e menor, joque novamente'))
            if jg !=pc:
                c = c + 1
        else:
            jg = int(input('\033[31m Errou \033[m, O numero e maior, jogue novamente '))
            if jg !=pc:
                c = c + 1
print('\033[32mVoce acertou\033[m, com {} tentativas'.format(c))

print('*'*10, ' Fim de jogo ', '*'*10)