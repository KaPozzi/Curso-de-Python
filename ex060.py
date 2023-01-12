n = int(input('Digite um numero para calcular seu Fatorial: '))
print(f'Calculando {n}!')
count = n
result = 1
while count > 0:
    print(f'{count} ', end='')
    print('x ' if count > 1 else '= ', end='')
    result *= count
    count -= 1
print(f'O Fatorial de {n} é {result}')