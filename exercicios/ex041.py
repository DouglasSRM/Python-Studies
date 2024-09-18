from datetime import date
ano1 = int(input('Insira seu ano de nascimento: '))
ano2 = date.today().year
idade = ano2 - ano1
print('CATEGORIA: ')
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=20:
    print('SENIOR')
else:
    print('MASTER')
