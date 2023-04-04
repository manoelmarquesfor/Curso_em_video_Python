# Crie um programa que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do python,
# so que fazendo a validacao para retorna apenas um valor numerico.


def leiaint(msg):
    while True:
        x = str(input(msg)).strip()
        if x.isnumeric():
            x = int(x)
            return x
            break
        else:
            print('\033[031mErro! Digite um numero inteiro valido.\033[m')

n = leiaint('Digite um numero: ')
print(f'O numero digitado foi {n}')