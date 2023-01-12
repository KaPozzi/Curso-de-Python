n = int(input('Digite um número inteiro: '))
print('''Qual será a base de conversão?')
[1] Para Binário
[2] Para Octal
[3] Para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{n} Convertido para Binário é: {bin(n) [2:]} ')
elif opção == 2:
    print(f'{n} Convertido para Octal é: {oct(n) [2:]} ')
elif opção == 3:
    print(f'{n} Convertido para Hexadecimal é: {hex(n) [2:]}')
else:
    print('Opção inválida, tente novamente')