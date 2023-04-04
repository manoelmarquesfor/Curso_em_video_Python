# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso a ctps for diferente de zero, o dicionario
# recebera tambem o ano de contratacao e o salario, Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (considere aposentadoria com 35 anos de carteira assinada)

from datetime import date

cadastro = {}

while True:
    cadastro['Nome'] = str(input('Nome: '))
    ano = int(input('Ano de nascimento: '))
    cadastro['idade'] = (date.today().year) - ano
    cadastro['ctps'] = int(input('Carteira de trabalho: (0 caso nao tenha)'))
    if cadastro['ctps'] == 0:
        break
    cadastro['ano_contratacao'] = int(input('Qual o ano de contratacao: '))
    cadastro['salario'] = float(input('Salario: R$ '))
    cadastro['aposentadoria'] = (cadastro['ano_contratacao'] - ano) + 35
    break
print('=-'*20)
#print(cadastro)
for key, valor in cadastro.items(): 
    print(f'{key} tem o valor {valor}')