from datetime import date

totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª Pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E tambem tivemos {totmenor} pessoas menores de idade')