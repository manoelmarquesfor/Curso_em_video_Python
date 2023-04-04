
def leiadinheiro(msg):
    while True:
        m = str(input(msg)).replace(',','.').strip()

        if m.isalpha() or m == '':
            print(f'\033[31m Erro: "{m}" e um preco invalido \033[m')

        else:
            m = float(m)
            break

    return m
