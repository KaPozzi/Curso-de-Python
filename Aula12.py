nome = str(input('Qual é o seu nome? '))
if nome == 'Kauã':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é normal no Brasil.')
elif nome in 'Ana, Claudia, Jessica, Ana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia, {nome}')