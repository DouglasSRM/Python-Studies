nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print(f'Sua média foi {media:.1f}')
if media < 5:
    print('\033[31mREPROVADO')
elif 5 >= media <= 6.99:
    print('\033[33mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')
