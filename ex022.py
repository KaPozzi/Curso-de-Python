nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')

up = nome.upper()
mn = nome.lower()
tt = nome.__len__()-nome.count(' ')
separa = nome.split()
fst = separa[0]
cont = fst.__len__()

print(f'Seu nome em maísculas é: {up}')
print(f'Seu nome em minúsculas é: {mn}')
print(f'O numero de caracteres é: {tt}')
print(f'O seu primeiro nome é {fst} e ele tem {cont} letras')