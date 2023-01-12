f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto =''.join(palavras)
inv = junto[::-1] 
print(inv)

if inv == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')