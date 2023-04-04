# Crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao mostre  a media entre todos os valores e qual foi
# o maior e o menor valores lidos, o programa deve perguntar ao usuario se ele quer ou nao continuar ao digitar valores.

parar = 'N'
c = 0
total = 0
lista = []
while parar not in 'S':
    n = int(input('Digite numeros '))
    parar = str(input('Gostaria de parar? [S/N]')).strip().upper()[0]
    lista = lista + [n]
    c = c + 1
    total = total + n
print('FIM')
print('O media foi {}'.format(total/c))
print('O maior numero da lista foi {} e o menor {}. '.format(max(lista),min(lista)))