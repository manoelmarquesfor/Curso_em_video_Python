#import pywhatkit as kt
#kt.sendwhatmsg("+558588512350", "Teste com o pywhatkit", 10, 6)
'''
def traduzir(msg):
    return msg.upper().replace('T', 'U')

n = str(input('Sequencia DNA: ')).upper()
print(f'Sequencia RNA = {traduzir(n)}')
'''
while True:
    dados = []
    dados2= []

    nome = str(input('Nome'))
    idade = int(input('Idade'))

    dados.append(nome)
    dados.append(idade)
    dados2.append(dados[:])
    dados.clear()

    print(dados)
    print(dados2)