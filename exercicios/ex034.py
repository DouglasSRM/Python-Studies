salario = float(input('Digite o salário: R$'))

if salario <= 1250:
    novosalario = salario + salario*15/100
else:
    novosalario = salario + salario *10/100

print(f'O novo salário é R${novosalario:.2f}')