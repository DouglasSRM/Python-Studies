velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade >= 81:
    multa = (velocidade - 80)*7
    print(f'Você foi multado. A multa é de R${multa:.2f}')
else:
    print('Você não foi multado!')
