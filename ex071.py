print('='*20)
print('BANCO CEV')
print('='*20)

valor = int(input('Qual valor você quer sacar? R$ '))
céd = 50
totcéd = 0

while True:
    if valor >= céd:
        valor -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cedulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if valor == 0:
            break
        


