tup = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atletico-MG', 'Fortaleza', 'São Paulo', 'América- MG', 'Botafog', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude'

print('-='*30)
print(f'Os cinco primeiros colocados são: {tup[0:5]}')
print('-='*30)
print(f'Os últimos 4 colocados são: {tup[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética {sorted(tup)}')
print('-='*30)
print(f'O time do Bragantino está na {tup.index("Bragantino")} posição')