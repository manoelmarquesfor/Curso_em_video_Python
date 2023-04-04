def linha(tam = 42):
    return '-'*tam


def menu(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menuOpcoes():
    lista = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa']
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c= c + 1
    print(linha())

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero valido\033[m')
        except KeyboardInterrupt:
            return 3
        else:
            return n

def opcoes():
    while True:
        opcao = leiaint('Sua opcao: ')
        if opcao == 1:
#            menu('OPCAO 1')
            lerArquivo(arq)
            return opcao

        if opcao == 2:
            menu('OPCAO 2')
            return opcao

        if opcao > 3:
            print('\033[031mOpcao invalida\033[m')

        if opcao == 3:

            return opcao


