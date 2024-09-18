peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura**2
print(f'Seu imc é {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está dentro do peso ideal.')
elif imc <= 30:
    print('Você está sobrepeso.')
elif imc <= 40:
    print('Você está na obesidade.')
else:
    print('Você está na obesidade mórbida.')
