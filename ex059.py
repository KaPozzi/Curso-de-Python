from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

o = 0 
while o != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar')
    [ 3 ] Maior
    [ 4 ] Novo número
    [ 5 ] Sair''')
    o = int(input('>>>>>>> Qual a sua opção?' ))
    if o == 1:
        print(f'A soma entre {n1} + {n2} é igual à {n1+n2}')
    elif o == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}.')
    elif o == 3:
        if n1 > n2:
            print(f'O maior numero é {n1}')
        else:
            print(f'O maior nnumero é {n2}')
    elif o == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif o == 5:
        print('Finalizando...') 
    else:   
        print('Opção inválida, tente novamente!')
    print('=-=' * 10)
    sleep (2)
print('Fim!') 