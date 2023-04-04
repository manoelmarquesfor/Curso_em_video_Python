#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual o valor sera
#o valor sacado (numero inteiro) e o programa deve informar quantas cedulas de cada valor sera entregue.
# obs: Considere que o caixa possui cedulas de 50, 20, 10 e 1.

valor = int(input('Qual o valor gostaria de sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
