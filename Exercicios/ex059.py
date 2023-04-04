# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

# Seu programa devera realizar a operacao solicitada em cada caso
from time import sleep

v1 = int(input('Diga um valor '))
v2 = int(input('Diga outro valor '))
m = 0
while m != 5:
    print('''Escolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do programa''')
    m = int(input('Oque deseja fazer?'))
    if m == 1:
        print('A soma de {} + {} vai ser {}'.format(v1, v2 , (v1 + v2)))
    elif m == 2:
        print('A multiplicado de {} * {} vai ser {}'.format(v1, v2, (v1 * v2)))
    elif m == 3:
        if v1 > v2 :
            n = v1
        else:
            n= v2
        print('O numero maior entre {} e {} vai ser o {}'.format(v1, v2, n))
    elif m == 4:
        print('Diga novos valores ')
        v1 = int(input('Diga um valor '))
        v2 = int(input('Diga outro valor '))
    elif m == 5:
        print('Finalizando')
        sleep(2)
    else:
        print('Tente novamente, opcao errada')
    print('=-'*14)
    sleep(1)
print('Fim')