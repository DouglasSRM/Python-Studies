import math
adj = float(input('Digite o cateto adjacente: '))
opo = float(input('Digite o cateto oposto: '))
hip = math.sqrt((adj**2) + (opo**2))
hi = math.hypot(opo, adj)
print(f'A hipotenusa é igual a {hi:.2f}')