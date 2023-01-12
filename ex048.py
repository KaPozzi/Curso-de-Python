soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n #soma = soma + n
        cont += 1 #soma = soma + 1
print(f'A soma de {cont} valores foi {soma}')