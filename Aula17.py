'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('Não encontrei o nº 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
###
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}...')
print('Cheguei ao final da Lista')

###

