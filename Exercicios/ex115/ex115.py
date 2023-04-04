# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema so vai ter 2 opcoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from funcoes import *
from arquivos import *

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    menu('Menu Principal')
    menuOpcoes()
    opcao = leiaint('Sua opcao: ')
    if opcao == 1:
        lerArquivo(arq)

    if opcao == 2:
        menu('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)


    if opcao > 3:
        print('\033[031mOpcao invalida\033[m')

    if opcao == 3:
        break



print()
print('Obrigado Volte sempre')