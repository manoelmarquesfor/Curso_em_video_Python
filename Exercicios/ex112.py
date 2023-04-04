# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado.Crie uma funcao chamada leiadinheiro() que seja capaz de funcionar como a funcao input(),
# mas com uma validacao de dados para aceitar apenas valores que seja monetarios.

from utilidadesCev import dado
from utilidadesCev import moeda

n = dado.leiadinheiro('Digite um valor: R$ ')
moeda.resumo(n, 35,22)