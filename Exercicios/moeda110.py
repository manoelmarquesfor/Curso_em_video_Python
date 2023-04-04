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

def resumo(num, aut=0, reducao=0):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preco analizado: \t{moeda(num)}')

    print(f'Dobro do valor: \t{dobro(num,True)}')
    print(f'Metade do valor: \t{metade(num, True)}')
    print(f'Diminuido {reducao}%: \t\t{diminuir(num,reducao, True)}')
    print(f'Aumentado {aut}%: \t\t{aumento(num, aut, True)}')

