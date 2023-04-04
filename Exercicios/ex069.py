#Crie um programa que leia Idade, sexo de varias pessoas. A cada pessoa cadastrada o programa devera perguntar se o usuario e
# quer ou nao continuar, No final mostre:
#Quantas pessoa tem mais de 18 anos  \ Quantos homens foram cadastrados.   \ Quantas mulheres tem menos de 20 anos.
print('='*10,'Cadastre uma pessoa', '='*10)

contIdade = 0
contHomens = 0
contMulheres = 0
while True:
    idade = int(input('Idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('M/F? ')).strip().upper()[0]
    p= ' '
    while p not in 'SN':
        p = str(input('Gostaria de continua? [S/N] ')).strip().upper()[0]
    print('='*30)

    if idade >= 18:
        contIdade = contIdade + 1
    if sexo == 'M':
        contHomens = contHomens +1
    if sexo == 'F' and idade < 20:
        contMulheres = contMulheres + 1
    if p == 'N':
        break

print(f'Tem {contIdade} pessoa com mais de 18 anos.')
print(f'Tem {contHomens} homens cadastrados.')
print(f'Tem {contMulheres} mulheres com menos de 20 anos.')