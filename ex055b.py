lista = []
for p in range(1, 6):
    lista.append(int(input(f'Peso da {p}ª pessoa: ')))

print(f'O MAIOR peso é de: {max(lista)}Kg')
print(f'O MENOR peso é de: {min(lista)}Kg')