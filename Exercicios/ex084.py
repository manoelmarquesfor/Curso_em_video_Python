# Faca um programa que leia o nome e peso de varias pessoas,guardando tudo em uma lista. no final mostre.
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
contagem = 0
mais_pesados = []
mais_leves = []
while True:
    dados.append(str(input('Qual seu nome? ')))
    dados.append(float(input('Qual seu peso? ')))
    pessoas.append(dados[:])
    dados.clear()
    contagem = contagem + 1
    pergunta = str(input('Deseja continar? [S/N] ')).strip().upper()[0]
    if pergunta =='N':
        break

for peso in pessoas:
    if peso[1] > 100:
        mais_pesados.append(peso[:])
    else:
        mais_leves.append(peso[:])

print(f'Foram contadas {contagem} pessoas')

if len(mais_pesados) == 1:
    print(f'A pessoa mais pesada e {mais_pesados[0][0]} com {mais_pesados[0][1]}kg ')
else:
    print(f'As pessoa mais pesada sao: ', end='')
    for nome in mais_pesados:
        print(f'{nome[0]} com {nome[1]}kg  ', end='')

#print(f'\nAs pessoas mais leves sao {mais_leves} ')
if len(mais_leves) == 1:
    print(f'\nA pessoa mais leves e {mais_leves[0][0]} com {mais_leves[0][1]}kg ')
else:
    print(f'\nAs pessoa mais leves sao: ', end='')
    for nome in mais_leves:
        print(f'{nome[0]} com {nome[1]}kg  ', end='')