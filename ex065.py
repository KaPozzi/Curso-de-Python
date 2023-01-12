cont = 'S'
count = sum = maior = menor = 0
while cont in 'Ss':
    num = int(input('Digite um número: '))
    cont = str(input('Quer continuar? [s/n] ')).upper().strip()[0]
    count += 1
    sum += num
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

med = sum / count
print(f'Você digitou {count} números e a média foi {med}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')