
"""

print("Qual é Seu nome?")
nome = input()

# print('Seja Bem-Vindo(a) %s' % nome.upper())
# print('Seja Bem-Vindo(a) {0}' .format(nome.upper()))
print(f'Seja Bem-Vindo(a) {nome.title()}')

ano = input('Em que ano você nasceu ? \n')

print(f'Sua idade é {2020 - int(ano)} anos')


numero = range(1, 10)
nome = 'Francisco'

for letra in enumerate(nome):
    print(letra[1])

for letra in range(11):
    print(letra)

for letra in range(1, 11):
    print(letra)

for letra in range(1, 11, 3):
    print(letra)

for letra in range(11, 0, -1):
    print(letra)


"""

for letra in range(11, 0, -1):
    print(letra)

