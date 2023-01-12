d = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes à começar uma viagem de {d} Km')

if d <= 200:
    pz1 = d * 0.50
    print(f'O preço da passagem é de R$ {pz1:.2f}')

else:
    pz2 = d * 0.45
    print(f'O preço da passagem é de R$ {pz2:.2f}')