valor = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Quanto você ganha? R$ '))
prazo = int(input('Em quantos anos você irá pagar? '))
minimo = salario * 30 / 100 #parcela

mês = prazo * 12
parcela = valor / mês

print(f'O valor da prestação será R${parcela:.2f} por mês')
if parcela <= minimo:
    print('Financiamento Liberado!')
else:
    print('Financiamento Negado.')