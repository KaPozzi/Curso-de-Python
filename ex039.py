from datetime import date

y = int(input('Digite o ano do seu nascimento: '))
data = date.today().year

idade = data - y
print(f'Você tem {idade} anos em {data}')

if idade < 18:
    print(f'Você ainda vai se alistar... falta {18 - idade} anos')
elif idade == 18:
    print('Hora de se alistar!')
else:
    print(f'Você já passou do tempo de alistamento há {idade - 18} anos')
    print(f'Deveria ter se alistado em {y + 18}')