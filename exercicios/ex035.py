r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 >= (r2+r3) or r2 >= (r1+r3) or r3 >= (r2+r1):
    print('As retas NÃO PODEM formar um triângulo!')
else:
    print('As retas PODEM formar um triângulo!')
