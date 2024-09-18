# SETANDO JOGADA DO PC #

from random import randint
pc = randint(1, 3)
if pc == 1:
    jk = 'pedra'
elif pc == 2:
    jk = 'tesoura'
elif pc == 3:
    jk = 'papel'

# Variável de resultado #

a = ('\033[33mEMPATE!')
b = ('\033[32mVOCÊ VENCÊU!')
c = ('\033[31mEU VENCI!')

# INICIO #

print('\033[35m===============JOKENPO===============')
player = input('\033[34mEscolha entre pedra, papel e tesoura... \n').lower().strip()
print(f'\033[34mEu escolhi {jk}!')

# CONDIÇÕES #

if player == 'pedra':
    if pc == 1:
        print(a)
    elif pc == 2:
        print(b)
    elif pc == 3:
        print(c)
elif player == 'tesoura':
    if pc == 1:
        print(c)
    elif pc == 2:
        print(a)
    elif pc == 3:
        print(b)
elif player == 'papel':
    if pc == 1:
        print(b)
    elif pc == 2:
        print(c)
    elif pc == 3:
        print(a)
else:
    print('\033[31mOPÇÃO INVALIDA')
