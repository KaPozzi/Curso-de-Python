from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))

ano = date.today().year
idade = ano - nasc
print(f'Você tem {idade} anos')

if idade <= 9:
    print('MIRIM')
elif 14 >= idade > 9:
    print('INFANTIL') 
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif 25 >= idade > 19:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')