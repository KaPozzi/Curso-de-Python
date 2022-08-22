import math
from re import A


'''b = float(input('Cateto Oposto: '))
c = float(input('Cateto Adjacente: '))
h = math.hypot(b, c)
print(f'A hipotenusa é: {h}')
'''
b = float(input('Cateto Oposto: '))
c = float(input('Cateto Adjacente: ')) 
h = (b ** 2 + c ** 2) ** (1/2)
print(f'A hipotenusa é: {h}')