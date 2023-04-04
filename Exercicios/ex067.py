# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera
#interrompido quando o numero digitado for negativo.

print('=='*20)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('==' * 20)
    if n <= 0:
        break
    for t in range(1,11):
        print(f'{n} x {t} = {n*t}')
print('='*17,'Fim', '='*17)