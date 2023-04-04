#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitador, espectivamente.
# Ao final, mostre o conteudo das tres listas geradas.


l1 = []
l2par = []
l3impar = []

while True:
    n = int(input('Diga um numero: '))
    if n not in l1:
        l1.append(n)
    d = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if d in 'N':
        break

for indice, valor in enumerate(l1):
    if valor % 2 == 0:
        l2par.append(valor)
    else:
        l3impar.append(valor)

print(f'Lista principal {l1}')
print(f'Lista par {l2par}')
print(f'Lista impar {l3impar}')

