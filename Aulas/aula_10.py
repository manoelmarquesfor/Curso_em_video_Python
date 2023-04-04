print('Vamos descobrir sua media.')
n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1+n2) / 2
print('Sua media foi {:.1f}' .format(m))
if m >= 6.0:
    print('Sua media foi otima. ')
else:
    print('Sua media foi pessima.')