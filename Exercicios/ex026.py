# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a"
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece a ultima vez


f = str(input('Diga uma Frase. ').strip().upper())
print('Quantos a tem na frase?', f.count('A'))
print('Qual a primeira posiccao que a aparece?',f.find('A') +1)
print('Qua a ultima posicao que a aparece', f.rfind('A')+1)
