from time import sleep
print('Gerador de PA')
sleep(1)
print('-='*10)
sleep(1)

f = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = f
count = 1
while count < 10:
    print(f'{termo} - ', end='')
    termo += r
    count += 1
print('FIM')