n = int(input('Digite um número para ver sua tabuada: '))
t = 1
for c in range(0,10):
    r = n * t
    print(f'{n} X {t:2} = {r}')
    t +=1
