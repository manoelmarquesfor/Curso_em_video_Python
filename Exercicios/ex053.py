# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo descondiserando os espacos.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} e {}' .  format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Nao temos um palindromo')