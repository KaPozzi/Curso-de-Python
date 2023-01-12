print('Analisador de Triângulos')

a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os seguimentos acima PODEM formar um triangulo.')

else:
    print(f'Os seguimentos acima NÃO PODEM formar um triâgulo.')

