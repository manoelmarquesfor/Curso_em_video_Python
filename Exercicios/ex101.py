# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa 
# retornando um valor literal indicando se uma pessoa tem voto OPCIONAL, OBRIGATORIO ou NEGADO nas eleicioes.

def voto(n):
    from datetime import date
    calculo = date.today().year - n
    print(calculo)
    if calculo <= 16:
        return f'O voto com {calculo} anos e NAO e OBRIGATORIO'
    elif calculo >= 18 and calculo < 65:
        return f'O voto com {calculo} anos e OBRIGATORIO'
    elif calculo >= 65 or calculo > 16 and calculo <= 18:
        return f'O voto com {calculo} anos e OPCIONAL'


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

