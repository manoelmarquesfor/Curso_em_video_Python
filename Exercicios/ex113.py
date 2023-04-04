# Reescreva a funcao leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitacao de um numero tipo invalido.
# Aproveite e crie tambem uma funcao leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[031mErro! Digite um numero inteiro valido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[031mO usuario preferiu nao digitar esse numero inteiro.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[031mErro! Digite um numero real valido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[031mO usuario preferiu nao digitar esse numero real.\033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um numero inteiro ')
real = leiaFloat('Digite um numero Real ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')