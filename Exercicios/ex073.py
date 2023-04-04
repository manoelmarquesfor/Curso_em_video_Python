# Crie uma tupla preenchida com os 20 primeiros colocado na tabela do Campeonato Brasileiro de futebol, na ordem de colocacao depois mostre:
#a) Apenas os 5 primeiros colocados.
#b) Os ultimos 4 colocados da tabela.
#c) Uma lista com os times em ordem alfabetica
#d) Em que posicao na tabela esta o time da chapecoense.



tabela = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino',
          'Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional',
          'São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
x = tabela.index('Chapecoense')

print(f'Os 5 primeiro colocados sao: {tabela[0:5]}')
print(f'Os 4 ultimos colocados da tabela sao: {tabela[-4:]}')
print(f'Times em ordem alfabetica{sorted(tabela)}')
print(f'O time Chapecoense esta na posicao {x + 1}')