p = float(input('Digite seu peso (Kg): '))
h = float(input('Digite sua altura (m): '))

imc = p / (h ** 2)

if imc < 18.5:
    print(f'IMC = {imc:.2f} - Abaixo do Peso')
elif 25 > imc >= 18.5:
    print(f'IMC = {imc:.2f} - Peso Ideal!')
elif 30 > imc >= 25:
    print(f'IMC = {imc:.2f} - Sobrepeso')
elif 40 > imc >= 30:
    print(f'IMC = {imc:.2f} - Obesidade')
elif imc >= 40:
    print(f'IMC = {imc:.2f} - Obesidade Morbida')