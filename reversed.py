"""

Reversed

"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

# Retorna um iteravel chamado List Reverse Iterator
print(res)
print(type(res))

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

#Podemos iterar sobre o reversed

for letra in reversed("Francisco Ricardo"):
    print(letra, end='')

print('\n')
#Fazendo sem uso do For
print(list(reversed('Francisco Ricardo')))
print(''.join(list(reversed('Francisco Ricardo'))))

print('Francisco Ricardo'[::-1])

for n in reversed(range(0, 10)):
    print(n)
