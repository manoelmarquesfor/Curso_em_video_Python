def metade(num, form=False):
    num = num/2
    return num if form is False else moeda(num)


def dobro(num, form=False):
    num = num * 2
    return num if form is False else moeda(num)


def aumento(num, taxa=0, form=False):
    num = num+(num*taxa/100)
    return num if form is False else moeda(num)


def diminuir(num, taxa=0, form=False):
    num = num - (num*taxa/100)
    return num if form is False else moeda(num)

def moeda(num, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')

def resumo(num, aumento=0, reducao=0):
    print(f'A metade de {moeda(p)} é {metade(p, True)}')
    print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
    print(f'Aumentado {aumento} de {moeda(p)} é {aumento(p, aumento, True)}')
    print(f'Reduzindo {reducao} de {moeda(p)} é {diminuir(p, reducao, True)}')