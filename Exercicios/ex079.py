# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista, caso o numero ja exista la dentro, ele nao sera adicionado.
#No final serao exibidos todos os valores unicos digitados em ordem crescente.


valor = []

while True:
    v = (int(input('Digite um valor: ')))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')

    continuar = str((input('Quer continuar? [S/N] '))).strip().upper()[0]
    if continuar in 'N':
        break

print('=-'*20)
print(f'Voce digito os valores {valor}')
valor.sort()
print(f'Os valores em ordem crescente sao {valor}')
