lar = float(input('Insira a largura em metros da parede: '))
alt = float(input('Insira a altura em metros da parede: '))
ar = lar*alt
lit = ar/2
print(f'A parede tem uma área de {ar:.3f} metros quadrados, sendo necessários {lit:.4f} litros de tinta para pintá-la')
