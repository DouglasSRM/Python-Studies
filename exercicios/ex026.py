frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece', frase.count('a'),'vezes!')

print('Tabém aparece pela primeira vez na posição',frase.find('a') + 1)

print('E pela última vez na posição', frase.rfind('a') + 1)
