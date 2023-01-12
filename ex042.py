print('Analisador de Triângulos')

a = float(input('Primeiro seguimtento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triangulo ', end='')
    if a == b == c:
        print('Equilátero.')
    elif a == b or a == c or b == c:
        print('Isóceles.')
    else:
        print('Escaleno.')

else:
    print('Os seguimentos acima NÃO PODEM formar um triangulo.')

