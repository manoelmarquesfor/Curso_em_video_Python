# Facar um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F. caso esteja errado, peca uma digitacao novamente ate ter um valor correto.

s = str(input('Qual seu sexo: [M/F]')).strip().upper()[0]

while s not in 'MF':
        s = str(input('Sexo invalido, Qual seu sexo? [M/F] ')).strip().upper()
print('Sexo {} registrado com sucesso.' .format(s))
