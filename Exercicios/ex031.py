# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preco da passagem, cobrando
# R$ 0.50 por km para viagens ate 200km e R$ 0.45 para viagens mais longa

distancia = float(input('Qual a distancia da sua viagem? ').strip())
if distancia <= 200:
    print('O valor da passagem para {}km e R${:.2f}' .format(distancia, distancia * 0.50))
else:
    print('O valor da passagem para {}Km e R${:.2f}R$ ' .format(distancia, distancia * 0.45))