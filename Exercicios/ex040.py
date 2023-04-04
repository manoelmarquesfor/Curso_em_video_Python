# Crie um programa que leia duas notas de um aluno e calcule sua media. mostrando uma mensagem no final de acordo com sua media.
# - Media abaixo de 5 reprovado,  - Media entre 5 e 6.9 recuperacao, - Media acima de 7 aprovado.

n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota?  '))
media = (n1 + n2) /2
if media < 5:
    print('Reprovado sua media foi {}'.format(media))
elif media > 5 and ((n1 + n2) / 2) < 7:
    print('Recuperacao sua media foi {}'.format(media))
elif media >= 7:
    print('Aprovado sua media foi {}'.format(media))