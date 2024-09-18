import math
angulo = float(input('Digite um ângulo para ver seu seno, cosseno e tangente: '))
n = math.radians(angulo)
print(f'seno = {math.sin(n):.2f}')
print(f'cosseno = {math.cos(n):.2f}')
print(f'tangente = {math.tan(n):.2f}')
