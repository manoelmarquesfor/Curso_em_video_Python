from funcoes import *

def arquivoExiste(nome):
    try:
        a = open(nome,'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except:
        print('ok')

def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler arquivo')
    else:
        menu('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever o dados')
        else:
            print(f'Novo registo de {nome} adicionado.')
            a.close()