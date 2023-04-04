# Faca um programa que tenha uma funcao chamada escreva(), que recebe um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.

def escreva(txt):
    print('~' * (len(txt)+4))
    print(f'  {txt}' )
    print('~' * (len(txt)+4))


frase = str(input('Diga uma frase. '))
escreva(frase)