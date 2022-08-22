d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pd = d * 60
pkm = km * 0.15
print(f'O total à pagar é de R$ {pd + pkm:.2f}')