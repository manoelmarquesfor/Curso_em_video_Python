#import cpf

#import pyautogui
import pyperclip
#pyperclip.copy

#n = input('Digite seu CPF. ')
#teste = cpf.checar(n)

#print('Seu CPF e ', teste)

#n = input('Se quiser gerar CPF digite 1 ')


def accum(l):
    d= []
    for c in l:
        l1 = l.index(c)
        d.append(c * (l1+1))
    x = '-'.join(d)
    return x.title()

print(accum('abcd'))