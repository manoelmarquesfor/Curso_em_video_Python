#Faca um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5!= 5x4x3x2x1=120


n = int(input('Diga um numero ' ))
c = n
f = 1
print('Calculando {}!= '.format(n),end='')
while c > 0:
    print('{}'.format(c),end='')
    print('x' if c > 1 else '= ', end='')
    f = f * c
    c = c - 1

print('{}'.format(f))

