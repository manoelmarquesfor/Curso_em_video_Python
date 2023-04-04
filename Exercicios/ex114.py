# Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado.


def versite():
    import urllib
    import urllib.request
    try:
        site = urllib.request.urlopen('http://www.pudim.com.br/')
    except:
        return 'O site Pudim nao esta acessivel no momento'
    else:
        return 'Consegui acessar o site Pudim com sucesso'


print(versite())