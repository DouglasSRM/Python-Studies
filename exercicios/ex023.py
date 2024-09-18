n = int(input('Digite um número de 0 a 9999: '))

unidade = n % 10
n = n // 10

dezena = n % 10
n = n // 10

centena = n % 10
n = n // 10

milhar = n % 10
n = n // 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')