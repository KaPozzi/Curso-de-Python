count = 0
countm = 0
countg = 0
while True:
    print('--'*20)
    print('Cadastre uma pessoa')
    print('--'*20)
    
    idade = int(input('Idade: '))
    if idade > 18:  
        count += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: ')).upper().strip()[0]
        if sexo == 'M':
            countm += 1
        if idade < 20 and sexo == 'F':
            countg += 1
    print('--'*20)
    destino = str(input('Quer continuar? [S/N] ')).upper().strip()
    if destino == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {count}')
print(f'Ao todo temos {countm} homens cadastrados.')
print(f'E temos {countg} mulheres com menos de 20 anos.')