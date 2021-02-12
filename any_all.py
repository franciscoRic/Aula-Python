"""
Any e All

all() -> retorna true se todos os elementos do interaveis forem verdadeiros ou se o interável esta vazio

#Exemplo all

print(all([0,  1, 2, 3, 4])) #Todos os numeros são verdadeiros ?

print(all([1, 2, 3, 4])) #Todos os numeros são verdadeiros ?

print(all([])) #Todos os numeros são verdadeiros ?

print(all([])) #Todos os numeros são verdadeiros ?

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra for letra in 'f' if letra in 'aeiou']))

any() -> Retorna true se qualquer elemento iterável for verdadeiro. Se o iteravel estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))

print(any([0, False, {}, (), []]))

print(any([letra for letra in 'f' if letra in 'aeiou']))

print(any([letra for letra in 'ai' if letra in 'aeiou']))