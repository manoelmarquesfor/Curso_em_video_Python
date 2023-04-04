#Crie um algoritimo que leia um numero e mostreu seu dobro, triplo e raiz quadrada

n1 = int(input('Escreva qualquer numero '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} e igual a {} o triplo e igual a {} e a raiz quadrada e igual a {:.2f}' .format(n1,d, t,r))
