# Faca um programa que leia o nome completo de uma pessoa, mostrando o primeiro e ultimo nome separadamente
# independendo to tamanho do nome
# EX: Ana maria de sousa     Primeiro = Ana     ultimo = Sousa


n = str(input('Qual seu nome? ').strip())
n1 = n.split()
print('Seu primeiro nome e: {} '.format(n1[0]))
print('Seu segundo nome e: {} ' .format(n1[-1]))