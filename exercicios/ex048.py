s = 0
n = 0
for c in range(1,501,2):
    if c % 3 == 0:
        n += 1
        s += c
print(f'foram {n} valores, resultado = {s}')

