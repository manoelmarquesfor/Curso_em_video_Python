# Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
# a)Quantos numeros foram digitados.
# b)A lista de valores ordenada de forma decrescente
# c)Se o valor 5 foi digitado e esta ou nao na lista


valor = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)

    decisao = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
    if decisao in 'N':
        break

print(f'Voce digitou {valor.__len__()} elementos')
print(f'Foi digitado os valores {valor}')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente e {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')

