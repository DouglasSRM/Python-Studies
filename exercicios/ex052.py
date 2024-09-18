a = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end= '')
        a += 1
    else:
        print('\033[31m', end= '')
    print(f'{c}', end= ' ')
print(f'\n\033[mO número {n} foi divisível {a} vezes, ', end= '')
if a == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO é primo!')