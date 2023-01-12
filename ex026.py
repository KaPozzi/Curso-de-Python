frase = str(input('Digite uma frase: ')).upper().strip()

print(frase)
letra = frase.count('A')
prim = frase.find('A')
ultima = frase.rfind('A')

print(f'A letra A aparece {letra} vezes na frase.')
print(f'A primeira letra A apareceu na posição {prim}')
print(f'A última letra A apareceu na posição {ultima}')