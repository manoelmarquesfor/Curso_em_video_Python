#Faca um programa que leia 5 valores numericos e guarde em uma lista.
#No final, mostre qual foi o meior e o menor valor digitado e as suas respectivas posicoes na lista


valores=[]

for posicao in range(0,5):
    valores.append(int(input(f'Digite um valor na posicao {posicao} : ')))
print(f'Os valores sao {valores}')
print(f'O maior valor e {max(valores)} e esta na posicao ', end='')
for indice , valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice}...', end='')
print(f'\nO maior valor e {min(valores)} e esta na posicao ', end='')
for indice , valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indice}...', end='')


