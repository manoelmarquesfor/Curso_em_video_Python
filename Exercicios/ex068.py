# Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando
# o total das vitorias consecutivas que ela conquistou no final do jogo.
from random import randint
print('=-='* 5, 'Vamos Jogar Par/Impar?','=-='*5 )
contador_jg = 0

while True:

    pc = randint(1, 10)
    jogador = int(input('Diga um valor '))
    vj = ' '
    while vj not in 'PI':
        vj= str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    s = (jogador + pc) % 2
    if s == 0:
        if vj == 'P':
            contador_jg = contador_jg + 1
        else:
            break
    elif s != 0:
        if vj == 'I':
            contador_jg = contador_jg + 1
        else:
            break
    print('-'*42)
    print(f'Voce jogou {jogador} e o computador {pc}, Total de {jogador + pc} e ', end='')
    print('par' if s == 0 else 'impar')
    print('-' * 42)
    print('Voce venceu.')
    print('Vamos jogar novamente...')
    print('-' * 42)


print('-' * 42)
print(f'Voce jogou {jogador} e o computador {pc}, Total de {jogador + pc} ')
print('-' * 42)
print(f'Voce perdeu! ')
print(f'GAME OVER! Voce venceu {contador_jg} vezes')
print('-' * 42)
