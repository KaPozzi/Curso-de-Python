import math


a = int(input('Digite o angulo desejado: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O Angulo {a} tem o SENO de {s:.2}')
print(f'O ângulo {a} tem o COSSENO de {c:.2}')
print(f'O ângulo {a} tem a TANGENTE de {t:.2}')