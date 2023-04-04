# Desenvolva um programa que leia seis numetos inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, desconsidere-o

s = 0
for n in range(0 , 6):
    c = int(input('Diga numeros'))
    if (c % 2 == 0):
        s = s + c
print('A soma dos numeros pares e {}'.format(s))