# Crie um programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indique o numero a calcular
# e o outro chamado show, que sera um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatoria.

def fatorial(a, b= False):
    if b == False:
        f = 1
        for c in range(a, 0, -1):
            f = f * c
        return f
    else:
        f = 1
        for c in range(a, 0, -1):
            f = f * c
            print(f'{c} x ', end='')
        return  f'0 = {f}'

def fatorial2(a, b = False):
    f = 1
    for c in range(a, 0, -1):
        if b:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')
        f = f * c
    return f




print(fatorial(5, True))
print(fatorial(5))


print(fatorial2(5, True))
print(fatorial2(5))

