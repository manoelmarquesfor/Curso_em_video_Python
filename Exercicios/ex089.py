# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individual.


boletim = []

while True:
    nome= str(input('Nome do aluno:'))
    nota_1 = float(input(f'Qual a 1ª nota: '))
    nota_2 = float(input(f'Qual a 2ª nota '))
    media = nota_1 + nota_2 / 2
    boletim.append([nome, nota_1, nota_2, media])
    pergunta = str(input('Continuar? [S/N]' )).strip().upper()[0]
    if pergunta in 'N':
        break

print('=-'* 15)
print('        Resultado')
print('=-'* 15)
print('Nº     Aluno           Media')
print('-'* 30)
for x in range(0 , len(boletim)):
    print(f'{x}     {boletim[x][0]:^8}          {boletim[x][3]}')
print('-'* 30)
while True:
    ver_nota = int(input('Mostrar nota de qual aluno? (999 para interrompe) '))
    if ver_nota >= len(boletim) or ver_nota == 999:
        print('Aluno nao encontrado')
        break
    print(f'Nota de {boletim[ver_nota][0]} são {boletim[ver_nota][1] , boletim[ver_nota][2]}')
    print('-' * 30)
print('Obrigado Volte sempre')