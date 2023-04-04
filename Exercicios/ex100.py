# Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somarPar(). A primeira funcao vai sortear 5 numeros
# e vai colocalos dentro da lista e a seunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior.

from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(0 , 5):
        x = randint(1,10)
        lista.append(x)
        print(f'{x} ', end='')
        sleep(0.4)
    print('Pronto')

def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros= []
sorteia(numeros)
somarPar(numeros)

