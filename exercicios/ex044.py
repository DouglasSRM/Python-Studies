preço = float(input('Qual o preço do produto? '))
condicao = input('''Qual a condição de pagamento?
A - À vista no dinheiro ou cheque
B - À vista no cartão
C - Até 2x no cartão
D - 3x ou mais no cartão
(Digite A, B, C ou D): ''').lower()
if condicao == 'a':
    pfinal = (preço*90/100)
elif condicao == 'b':
    pfinal = (preço*95/100)
elif condicao == 'c':
    pfinal = (preço)
elif condicao == 'd':
    pfinal = (preço*120/100)
print(f'O preço a ser pago é R${pfinal:.2f}')
