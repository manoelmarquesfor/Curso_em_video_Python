# Faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario. No final, mostre o conteudo da estrutura na tela.

aluno = {}

for p in range(0,1):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Media de {aluno["nome"]} '))
    if aluno['media'] <= 4:
        aluno['situacao'] = 'reprovado'
    elif aluno['media'] < 7:
        aluno['situacao'] = 'recuperacao'
    else:
        aluno['situacao'] = 'aprovado'
print('=-'*15)
print(f'Nome e igual a {aluno["nome"]} ')
print(f'Media e igual a {aluno["media"]} ')

if aluno['situacao'] == 'reprovado':
    print(f'Situacao e igual a \033[31m REPROVADO \033[m')

elif aluno['situacao'] == 'recuparacao':
    print(f'Situacao e igual a \033[33m RECUPERACAO \033[m')

else:
    print(f'Situacao e igual a \033[32m APROVADO \033[m')

