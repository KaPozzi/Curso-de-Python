nrs = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))
print(f'Você digitou os valores {nrs}')
print(f'O valor 9 apareceu {nrs.count(9)} vezes')
if 3 in nrs:
    print(f'O valor 3 apareceu na posição nº {nrs.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram:', end=' ')
for n in nrs:
    if n % 2 == 0:
        print(n, end=' ')