# Aula 19 - Dicionario

# pode declarar um dicionario de 2 formas
# forma 1:  variavel = {}  /  filme = {}
# forma 2: variavel = dict()  / filme = dict()


filme = {'titulo' : 'Star Wars', 'ano' : 1977 , 'diretor' : 'George Lucas'}
#itens {   keys  :    values     }


#OBS: NAO PODE ESQUECER DAS ASPAS PARA DECLARAR AS KEYS
# item e tudo que esta no dicionario valores e chaves(keys)   print(filme.items())
# keys e o indicador no exemplo e Titulo, ano e diretor    print(filme.keys())
# values e o valor das keys no exemplo e Star Wars para titulo, 1977 para o ano, George Lucas para o diretor.  print(filme.values())
# : significa que a key tem esse valor

# comando del variavel[key]   apaga a chave e o valor
# variavel[key] = values   adiciona uma key e valor ao dicionario(variavel)


print(filme.values())
print(filme.keys())
print(filme.items())

for key, values in filme.items():
    print(f'O {key} e {values}')

pessoas = {'nome':'Manoel', 'sexo':'M' ,'idade':'27'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')


del pessoas['idade']   # removendo idade da variavel
pessoas['peso'] = 120  # adicionando peso a variavel

print(pessoas)

for k,v in pessoas.items():
    print(f'{k} = {v}')
# notase que a key idade foi apagada


# Adicionando um dicionario a uma lista

brasil = []
estado1 = {'uf' : 'Ceara' , 'sigla' : 'CE'}
estado2 = {'uf' : 'Piaui' , 'sigla' : 'PI' }
brasil.append(estado1)
brasil.append(estado2)

print(brasil)  # vemos que a lista chamada brasil com 2 dicionario que e estado 1 e estado 2
print(brasil[0]['uf']) # vemos posicao 0 da lista com a uf do dicionario

estado = dict()
Brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa '))
    estado['sigla'] = str(input('Sigla do estado '))
    Brasil.append(estado.copy())     # para copiar no dicionario usada o .copy (no caso aqui esta copiando a lista para o dicionario)
print(Brasil)
for e in Brasil:
    for v in e.values():
        print(v , end=' ')
    print()