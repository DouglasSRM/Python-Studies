from datetime import date
ano1 = int(input('Insira o ano em que você nasceu: '))
ano2 = date.today().year
idade = ano2 - ano1

if idade < 18:
    print('Ainda não é o momento de você se alistar no serviço militar.')
    print(f'Faltam {18 - idade} ano(s) para você se alistar!')
elif idade == 18:
    print('Está no momento para você se alistar no serviço militar!')
else:
    print('Já passou do momento de você se alistar no serviço militar.')
    print(f'Já passaram {idade - 18} ano(s) do prazo para você se alistar!')
