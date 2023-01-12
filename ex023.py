num = int(input('Informe um número: '))

un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
mil = num // 1000 % 10

print(f'Analisando o número {num}...')
print(f'Unidade: {un}')
print(f'Dezena: {dz}')
print(f'Centena: {ct}')
print(f'Milhar: {mil}')