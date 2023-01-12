cap = float(input('Qual é o salário do funcionário? R$'))

if cap <= 1250:
    ajust = (cap * 0.15) + cap
    print(f'Quem ganhava R${cap:.2f} passa a ganhar R${ajust:.2f} agora.')

else:
    ajust2 = (cap * 0.10) + cap
    print(f'Quem ganhava R${cap:.2f} passa a ganhar R${ajust2:.2f} agora.')