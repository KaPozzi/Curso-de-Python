nome = str(input('Digite o seu nome completo: ')).strip().split()

prim = nome[0]
ult = nome[-1]

print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {prim}')
print(f'Seu último nome é {ult}')