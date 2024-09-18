nome = str(input('Digite seu nome completo: '))
nt = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
print(f'O primeiro nome é {nt[0]} e ele tem {len(nt[0])} letras')
