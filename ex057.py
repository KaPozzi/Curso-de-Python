s = str(input('Informe seu sexo (M/F): ')).strip().upper() [0] #fatiando, pegando a primeira letra do que for digitado.
while s not in 'FfMm':
    s = str(input('Dados inválidos, tente novamente: ')).strip().upper()
print(f'Sexo {s} cadastrado com sucesso.')