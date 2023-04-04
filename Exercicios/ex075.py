# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posicao foi digitado o primeiro valor 3.
# c) Quais foram os numeros pares.


e = (int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite o ultimo numero: ')))

d = e.count(3)

print(f'Voce digitou os valores {e}')

print(f'O valor 9 apareceu {e.count(9)} vezes')
if d >= 1:
    print(f'O valor 3 esta na posicao {e.index(3)+1}.')
else:
    print('O valor 3 nao foi digitado nenhuma vez. ')
print('Os valores pares digitador foram ', end='')
for n in e:
    if n % 2 == 0:
        print(n, end=' ')
