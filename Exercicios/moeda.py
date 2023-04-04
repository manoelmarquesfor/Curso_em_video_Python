def metade(num):
    num = num/2
    return num


def dobro(num):
    num = num * 2
    return num


def aumento(num, taxa=0):
    num = num+(num*taxa/100)
    return num


def diminuir(num, taxa=0):
    num = num - (num*taxa/100)
    return num

def moeda(num, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')