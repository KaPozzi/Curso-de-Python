t1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = t1 + (10 - 1) * r
for pa in range(t1, decimo + r, r):
    print(pa, end=', ')
print('Acabou')
