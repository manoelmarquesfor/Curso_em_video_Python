# crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o ususario digitar o valor 999, que e a condicao final mostre quantos numeros foram digitados
# e qual foi a soma entre elas(desconsiderando o flag)


n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Diga um numero, para parar digite 999 '))
    c = c + 1
    s = s + n
    if n == 999:
        print('\033[32mFim do app\033[m')

print('Foram digitados {} vezes {}'.format(c -1, s - 999))

'''
ou 
n = 0
c = 0
s = 0
n = int(input('Diga um numero, para parar digite 999 '))
while n != 999:
    n = int(input('Diga um numero, para parar digite 999 '))
    c = c + 1
    s = s + n
    if n == 999:
        print('\033[32mFim do app\033[m')

print('Foram digitados {} vezes {}'.format(c , s))
'''