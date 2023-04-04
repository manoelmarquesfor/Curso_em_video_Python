c = 0
s = 0
while True:                                                 #repeticao while True so para quando o breack e acionado que no caso e 999
    n = int(input('Diga um numero. '))                      # oq acontece apos o break nao e feito (somado ou contado)
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'Voce digito {c} vezes, e todos somados fica {s}')          #print apos aula 15 (atualizacao do python, simplicando.
print('Voce digito {} vezes, e todos somados fica {}'.format(c,s)) #print de todo o curso ate a aula 14, modelo antes da atualizacao

