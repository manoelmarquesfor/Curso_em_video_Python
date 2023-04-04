#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao(sem usar o sort()).
#No final, mostre a lista ordenada na tela.

valor = []

for c in range(0,5):
    n = int(input('Diga um valor'))
    if c == 0 or n > valor[-1]:
        valor.append(n)
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                break
            pos = pos + 1
print('-='*30)
print(f'Os valores digitados em ordem foram{valor}')


