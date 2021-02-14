"""

Min e Max

max() => Retorna o maior valor em um iteravel ou retorna o maior valor em dois ou mais elementos


lista = [2, 8, 4, 99, 34, 129]

print(max(lista))

dicionario = {'a': 1, 'b': 158, 'c': 45, 'd': 58, 'e': 15}

print(max(dicionario))

print(max(dicionario.values()))

val1 = int(input('Informe o Primeiro Valor: '))
val2 = int(input('Informe o o Segundo Valor: '))

print(max(val1, val2))

"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Sink Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock', 'tocou': 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])



