ValorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos você vai pagar? '))

meses = anos * 12
parcela = ValorCasa/meses

if parcela < (salario*30/100):
    print(f'A parcela mensal é de R${parcela:.2f}')
else:
    print('O emprestimo foi negado! Infelizmente você não completou os requisitos.')
