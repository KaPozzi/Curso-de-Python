from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)

print(f'{" Jogo do Jokenpô ":=^40}')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
e = int(input('Qual é a sua jogada? '))

print('-=' * 10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(2)
print(f'Você jogou {itens[e]}')
print(f'O PC jogou {itens[pc]}')

print('-=' * 10)

if e == 0 and pc == 0:
    print('Empate')
elif e == 1 and pc == 0:
    print('Você ganhou!')
elif e == 2 and pc == 0:
    print('Você perdeu.')
elif e == 0 and pc == 1:
    print('Você perdeu')
elif e == 1 and pc == 1:
    print('Empate')
elif e == 2 and pc == 1:
    print('Você ganhou!')
elif e == 0 and pc == 2:
    print('Você ganhou!')
elif e == 1 and pc == 2:
    print('Você perdeu.')
elif e == 2 and pc == 2:
    print('Empate')