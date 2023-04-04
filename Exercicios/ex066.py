# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999,
# que e a condicacao de parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o flag(sinal de parada)

contador = 0
soma = 0

while True:
    n = int(input('Diga um numero,(999 para parar) '))
    if n == 999:
        break
    contador = contador + 1
    soma = soma + n
print(f'A soma dos {contador} valores foi {soma}')