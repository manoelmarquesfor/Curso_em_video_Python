# Crie um programa que tenha uma tupla com varias palavras(nao usar acentos), depois disso vc deve mostrar para cada palavra quais sao as suas vogais.

palavras = ('agua','sabao','pneu','macarrao','feijao','impressora')

for p in palavras:
    print(f'\nNa palavra {p} temos: ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')