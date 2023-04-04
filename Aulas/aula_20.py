# Aula de funcao

def mostralinha():    # sintax  def nomedafuncao(parametro)
    print('-'*20)      # oq ela faz

def titulo(texto):
    print('-' *20)
    print(texto)
    print('-' *20)

def soma(a , b):
    print(f'A = {a} , B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

def separar():
    print('#'*20)

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim! ')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos = pos + 1


#def 01
mostralinha()
print('Sistema de alunos')
mostralinha()
print('Cadastro de aluno')
mostralinha()

separar()

#def02
titulo('Sistema de alunos')
titulo('Cadastro de aluno')

separar()

soma(5 , 10)
mostralinha()
soma(6 , 15)
mostralinha()
soma(10 , 60)

separar()

contador(2, 8, 4, 5, 9)
contador(9, 7, 6,)
contador(2)

separar()

valores =  [9, 5, 6, 7, 2, 0]
print(valores)
dobra(valores)
print(f'Os valores dobrados sao: {valores}')