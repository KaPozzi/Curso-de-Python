n = int(input('Digite um número [999 para parar]: '))
count = 0
sum = 0
while n != 999:
    count += 1
    sum += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count} números e a soma deles é {sum}')