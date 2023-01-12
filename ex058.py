from time import sleep
from random import randint

print('Sou seu computador...')
sleep (2)
print('Acabei de Pensar em um número entre 0 e 10')
sleep (2)
print('Será que você consegue adivinhar qual foi?')
n = int(input('Qual é o seu palpite? '))

r = randint(0, 11)

while n is not r:
    if n < r:
        print('Um pouco mais...')
    elif n > r:
        print('Um pouco menos...')
    else:
        print('Você acertou!')  