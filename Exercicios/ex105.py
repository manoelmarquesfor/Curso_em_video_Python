# Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retorna um dicionario com as seguintes informacoes.
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situacao(opcional)

#Adicione tb as docstring da funcao.
def notas(* num, sit=False):
    total = len(num)
    maior = max(num)
    menor = min(num)
    media = sum(num)/total
    if sit:
        if media < 2:
            sit = 'Sem futuro'
        elif media <6:
            sit = 'Ruim'
        else:
            sit = 'Otima'
        return {'total': total, 'maior':maior, 'menor': menor, 'media': media, 'situacao':sit}
    else:
        return {'total': total, 'maior': maior, 'menor': menor, 'media': media}


resp = notas(5.5, 9.5, 10.0, 6.5, sit=True)
print(resp)