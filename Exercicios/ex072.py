#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
# seu programa devera ler um numero pelo teclado( entre 0 e 20) e mostralo por extenso.

extenso = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis', 'sete','oito','nove','dez','onze','doze', 'treze', 'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
'''
como eu fiz

n = 22
while n > 20:
    n = int(input('Diga um numero entre 0 e 20 '))
print(extenso[n]) '''

'''
professor fez 

while True:
    n = int(input('Diga um numero entre 0 e 20 '))
    if n <=0 or n <=20:
        break
    print('Tente novamente. ', end='')

    while True:
        pergunta = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
        if pergunta in 's':
            break


print(extenso[n])
'''
#professor pediu pra adicionar

while True:
    n = int(input('Diga um numero entre 0 e 20 '))
    if n < 0 or n > 20:
        n = int(input('Tente novamente. Diga um numero entre 0 e 20 '))

    if n < 0 or n <= 20:
        print(extenso[n])

    pergunta = str(input('Deseja continuar? S/N  ')).strip().upper()[0]
    if pergunta in 'N':
        break
print('Fim do programa')