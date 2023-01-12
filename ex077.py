tup = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for word in tup:
    print(f'\nNa palavra {word.upper()} temos', end=' ')
    for letra in word:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
