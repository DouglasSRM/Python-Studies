"""from random import choice

lista = [int(0), int(1), int(2), int(3), int(4), int(5)]
n = choice(lista)

t = int(input('O computador gerou um número de entre 0 e 5, tente adivinhar qual é: '))

if t == n:
    print(f'Você acertou! O número era {n} :)')
else:
    print(f'Você errou! O número era {n} :(') """

from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[34m-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('\033[32mEm que número eu pensei? '))
print('\033[1;31mPROCESSANDO...\033[m')
sleep(1.54)
if jogador == computador:
    print('\033[32mPARABÉNS! Você venceu.')
else:
    print(f'\033[31mGanhei >:)! O número que pensei foi o {computador}')
