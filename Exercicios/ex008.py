#Escreva um programa que leia os valores em METROS e exita convertido em CENTIMETROS.


n1 = float(input('Quantos metros? '))
d = n1 * 10
c = n1 * 100
m = n1 * 1000
dc = n1 /10
cm = n1 / 100
k = n1 / 1000
print('Voce tem {} metros e {:.0f} decimetros e {:.0f}centimetros e {:.0f} milimetros'.format(n1,d,c,m))
print('Voce tem {} metros e {}DM e {}HM e {} Kilometros' .format(n1,dc,cm,k))
