print(f'{"HOLO ELETRONICS":=^40}')
p = float(input('Preço do Produto: R$ '))
print('''FORMAS DE PAGAMENTO
[1] - Dinheiro/Cheque
[2] - Cartão
[3] - 2x no Cartão
[4] - 3x ou mais''')

cond = int(input('Opção: '))

if cond == 1:
    print(f'Você terá 10% de desconto, o valor ficará R${p - (p * 0.10)}')
elif cond == 2:
    print(f'Você terá 5% de desconto, o valor ficará R$ {p - (p * 0.05)}')
elif cond == 3:
    print(f'Não há desconto')
    print(f'A forma de pagamento será em 2x de R${p / 2:.2f}')
elif cond == 4:
    a = int(input('Em quantas parcelas? '))
    print(f'Terá 20% de juros, o valor total ficará: R${(p * 0.20) + p:.2f}')
    print(f'A parcela será em {a}x de {((p * 0.20) + p) / a:.2f}')
else:
    print('Opção Inválida de Pagamento, tente novamente...')
