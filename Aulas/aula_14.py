# Aula de while
'''
c = 1
while c < 10:     # Enquanto a variavel C for menor que 10
    print(c)
    c = c + 1      # variavel C = C + 1 que significa que acada vez ela vai adicionando + 1 ao valor de c
                   # ate chegar no valor que esta no while
print('Acabou')
'''

n = 1
impar = 0
par = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Voce digito {} par e {} impar'.format(par,impar))
