"""

Zip

zip() => Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteravei passandos como entrada em pares

#Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
zip2 = zip(lista2, lista1)
zip3 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(zip2)
print(type(zip2))

print(list(zip1))

print(tuple(zip2))

print(dict(zip(lista1, lista2)))

"""
#Exemplos mais complexos
prova1 = [80, 90, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

#Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))