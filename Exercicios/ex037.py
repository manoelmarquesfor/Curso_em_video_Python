# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a sabe se conversao.
# 1 - para binario   2 - para octal      3 - para hexadecimal.

numero = int(input('Digite um numero.'))
c = int(input('Escolha para qual fazer a conversao: 1 - Binaeio , 2- Octal , 3 - Hexadecimal  '))
if c == 1:
    print(bin(numero)[2:])
elif c == 2:
    print(oct(numero)[2:])
elif c == 3:
    print(hex(numero)[2:])
