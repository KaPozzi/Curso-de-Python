prod = ('Lápis', 2.99, 'Caneta', 5.99, 'Borracha', 3.00,
 'Caderno', 27.90, 'Penal', 10.00, 'Transferidor', 6.99,
  'Compasso', 9.99, 'Mochilha', 89.90, 'Livro', 32.90)
print('-'*40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-'*40)
for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end='')
    else:
        print(f'R${prod[pos]:>7.2f}')
print('-'*40)