# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais algum termo, o programa encerra quando ele disser que quer mostrar 0 termo.

p = int(input('Primeiro termo: '))
r = int(input('Razao '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo = termo + r
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Prograssao finalizada com {} termos mostrados.'.format(total))
