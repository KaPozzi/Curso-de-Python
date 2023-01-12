import random

pc = random.randint(0, 5)
print('Estou pensando em um numero de 0 a 5...')
n1 = int(input('Qual você acha que é? '))

if n1 == pc:
    print('Acertou abestado')
else: 
    print(f'Você perdeu. eu pensei no numero {pc}')