from random import randint

tup = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram:')
for n in tup:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi: {max(tup)}')
print(f'O menor valor sorteado foi: {min(tup)}')