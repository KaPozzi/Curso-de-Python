from itertools import count


somaidade = 0
mediaidade = 0
nomehmv = 0
idademv = 0 
totmulher20 = 0

for c in range(1, 5):
    print(str(f'-----{c}ª Pessoa -----'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        idademv = idade
        nomehmv = nome
    if sexo in 'Mm' and idade > idademv:
        idademv = idade
        nomehmv = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1


mediaidade = somaidade / 4
    
print(f'A média de idade do Grupo é: {mediaidade}')
print(f'O nome do homem mais velho é {nomehmv} e ele tem {idade} anos')
print(f'Há {totmulher20} Mulheres tem menos de 20 anos.')