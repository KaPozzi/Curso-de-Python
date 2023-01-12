n1 = float(input('Primeira nota: '))
n2 = float(input('Segundanota: '))

lista = [n1, n2]
media = sum(lista) / len(lista)
print(f'{media}')

if media < 5.0:
    print('Reprovado.')
elif 7 > media > 5:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado!')