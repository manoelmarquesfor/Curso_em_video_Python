#Listas
'''
num = [2,5,9,1]
num[2] = 3   # substitui o 2 elemento da lista por 3
print(num)
num.append(7)  # adiciona o numero 7 no final da lista
print(num)
num.sort()   # vai colocar a lista em ordem crescente
print(num)
num.sort(reverse=True)   # usando o reverse+True coloca em ordem contraria
print(num)
num.insert(2,0)  # insere o 0 na seguna posicao diferente do primeiro comando que substituiu
print(num)
num.pop()         #exclui o ultimo elemento da lista
print(num)
num.pop(2)          #exclui o elemento que estiver dentro dos parenteses (no caso o elemento 2)
print(num)
num.remove(5)    # usado para remover da lista varrendo do inicio para o fim(so remove a primeira ocorrencia)
print(num)

num2 = []   # [] declara que e uma lista, podendo tb ser declaro list()
num2.append(6)
num2.append(8)
num2.append(1)
for c, v in enumerate(num2):
    print(f'Na posicao {c} encontrei o valor {v}')

# para adicionar valores na lista usando o for

valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores):
    print(f'Na posicao {posicao} temos o valor {valor}.')
'''
a = [2,3,4,7]
b = a               # b e igual a sendo assim oq mudar em b tb vai mudar em a (as 2 estao ligadas)
b= a[:]             # b recebe valor de a sendo assim oq mudar em b nao vai mudar em a, essa copia e feita usando [:]
b[2] = 0
print(f'Lista a{a}')
print(f'Lista b{b}')

