print('Digite três números abaixo!')
n1 = int(input('1°: '))
n2 = int(input('2°: '))
n3 = int(input('3°: '))
# Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

lista = [n1, n2, n3]
lista.sort()
print(f'O maior número é {lista[2]} e o menor é {lista[0]}')
