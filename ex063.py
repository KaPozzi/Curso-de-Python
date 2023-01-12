print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2} - ', end='')
count = 3
while count <= n:
    count += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} - ', end='')
print('FIM')