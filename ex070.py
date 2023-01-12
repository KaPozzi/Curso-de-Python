print('--'*20)
print('Loja Super Baratão')
print('--'*20)

price = 0
cheap = expensive = sum = count = 0
countc = 0
productc = ' '
while True:
    product = str(input('Nome do Produto: '))
    price = int(input('Preço: R$ '))
    if count == 1:
        cheap = price
        productc = product
    else:
        if cheap < price:
            cheap = price
            productc = product
    count += 1
    sum += price
    if price > 1000:
        countc += 1
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if ask == 'N':
        break
print('------------FIM DO PROGRAMA------------') 
print(f'O total da compra foi de R$ {sum}')
print(f'Temos {countc} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {productc} que custa R$ {cheap}')
           

