# Tratamentos e Excecoes

try:    # try quer dizer faça algo
    a = int(input('Numerador: '))
    b = int(input('Denominador '))
    r = a / b

except (ValueError, TypeError):          # except quer dizer excessao
    print('Tivemos um problema com os tipos de dados digitado')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por ZERO')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:                   # se nao der Erros execute
    print(f'O resultado e {r:.1f}')
finally:                # finally sempre vai acontecer independente de erro ou nao
    print("Volte sempre! Muito Obrigado")
    
