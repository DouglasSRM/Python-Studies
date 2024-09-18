cidade = str(input('Digite o nome de uma cidade: ')).strip()

cidade = cidade.lower()

c1 = cidade.split()[0]

if('santo' in c1):
    print('O primeiro nome da cidade é Santo!')
else:
    print('O primeiro nome da cidade não é Santo :(')
