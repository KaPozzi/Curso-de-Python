print('Gerador de PA')
print('-=' * 10)

f = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
term = f
count = 1
new = 10
total = 0
while new != 0:
    total += new
    while count <= total:
        print(f'{term} - ', end='')
        term += r
        count += 1
    print('Pausa')
    new = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')