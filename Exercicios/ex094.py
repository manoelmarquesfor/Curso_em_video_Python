# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No inal mostre:
# a) Quantas pessoas foram cadastradas.
# b) A media de idade do grupo.
# c) Uma lista com todas as mulheres.
# d) Uma lista com todas as pessoas com idade acima da media.

cadastro = []
ficha = {}
soma = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if ficha['sexo'] in 'MF':
            break
        print('ERRO! Por favor, apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))
    soma = soma + ficha['idade']
    cadastro.append(ficha.copy())
    ficha.clear()
    while True:
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if pergunta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if pergunta in 'N':
        break
print(cadastro)
print('=-'*20)
print(f' - O grupo tem {len(cadastro)} pessoas ')
media = soma / len(cadastro)
print(f' - A media de idade do grupo e {media:5.2f} anos.')
print(' - As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}' , end='')
print()
print(' - Lista das pessoas que estao acima da media: ', end= '' )
for p in cadastro:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')
