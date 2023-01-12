from random import randint
print('-='*30)
print('Vamos jogar Par ou Ímpar!')
print('-='*30)
pc = sum = 0
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    print('--'*30)
    pc = randint(1, 10)
    sum = jogador + pc
    print(f'Você jogou {jogador} e o computador {pc}. Total de {sum}', end=' ')
    print('DEU PAR' if sum % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if sum % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if sum % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar Novamente...')
print(f'Game Over, você venceu {v} vezes.')