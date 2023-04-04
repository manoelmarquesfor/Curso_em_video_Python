#Desenvolva uma logica que leia o peso e a altura de uma pessoa. Calcule seu imc e mostre seu status, de acordo com a tabela abaixo.
#Abaixo de 18.5: Abaixo do peso  / Entre 18.5 e 25 : Peso ideal   /  25 ate 30 sobrepeso  / 30 ate 40 obesidade  / Acima de 40 obsidade morbida.
import time

print('=='*10, 'vamos Calcular seu IMC','=='*10)

peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (M) '))
imc = peso / (altura * altura)
print('Calculando...')
time.sleep(1)
if imc < 18.5:
    print('Abaixo do peso, pois seu IMC e {:.1f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu peso e o ideal {}'.format(imc))
elif imc > 25 and imc <=30:
    print('Voce tem sobrepeso pois seu imc e {:.1f}'.format(imc))
elif imc > 30 and imc <=40:
    print('Voce tem obesidade pois seu imc e {:.1f}'.format(imc))
elif imc > 40:
    print('Voce tem obesidade morbida pois seu imc e {:.1f}'.format(imc))

print('=='*32)