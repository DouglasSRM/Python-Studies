termo1 = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo = termo1 + (10 - 1) * razao
print('Os primeiros 10 termos da PA são:')
for c in range(termo1, decimo + razao, razao):
    print(c)