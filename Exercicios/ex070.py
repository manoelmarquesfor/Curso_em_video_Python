#Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar. no final mostre.
# Qual e o total gasto na compra.  \  Quantos produtos custao mais de 1000 \   Qual e o produto mais barato.

precoTotal = 0
totalmil = 0
contador = 0
menor = 0
barato = ''
while True:
    produto = str(input('Produto? '))
    preco = float(input('Preço? R$ '))
    contador = contador + 1

    if preco > 1000:
        totalmil = totalmil + 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Continuar [S/N] ')).strip().upper()[0]
    precoTotal= precoTotal + preco
    if pergunta == 'N':
        break
print(f'Total da compra foi {precoTotal}')
print(f'Tem {totalmil} custando mais de R$ 1000')
print(f'O produto mais barato e {barato} e custa {menor}')