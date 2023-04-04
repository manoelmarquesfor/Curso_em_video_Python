# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
# No final, mostre uma listagem de precos, organizando os dados em forma tabular.


l = ('Aro', 75.00, 'Pneu', 250.00, 'Rolamento', 18.00, 'Lampada', 30.00 )

for pos in range(0 , len(l)):
    if pos % 2 == 0:
        print(f'{l[pos]:.<30}',end='')
    else:
        print(f'R${l[pos]:<7.2f}')
