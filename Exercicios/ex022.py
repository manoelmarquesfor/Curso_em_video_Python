# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# quantas letras ao todo sem considerar espassos
# Quantas letras tem o primeiro nome


frase = input('Digite uma frase  ')
s = frase.replace(' ','')
p = frase.split()
print('Sua frase com todas aa letras maiusculas', frase.upper())
print('Sua Frase com todas as letras minusculas' ,frase.lower())
#print(len(frase.strip()))
print('Sua frase tem {} sem considerar os espacos' .format(len(s)))

print('Sua frase tem {} e tem {} letras no primeiro nome' .format(p[0],len(p[0])))
