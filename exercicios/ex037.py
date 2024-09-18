number = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')
option = int(input('Sua opção: '))
if option == 1:
    print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}')
elif option == 2:
    print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}')
elif option == 3:
    print(f'{number} convertido para {hex(number)[2:]}')
else:
    print('Opção inválida, tente novamente.')
