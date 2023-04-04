# Faca um mini sistema que utilize o INTERACTIVE HELP do Python. O usuario vai digitar o comando e o manual vai aparecer
#Quanto o usuario digitar a palavra "FIM", o programa se encerrara.

def sis(msg):
    return help(msg)

def titulo(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


while True:
    titulo('Sistema de ajuda HelPython')
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        sis(comando)
titulo('Volte sempre')