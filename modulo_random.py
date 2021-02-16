"""

Modulo Randon

from random import random
from random import uniform

print(random())

#Gera valores Reais ponto flutuante
for x in range(10):
    print(uniform(3, 7))

#Gera numeros inteiros pseudo-aleatorio
from random import randint

for u in range(6):
    print(randint(1, 61), end=', ')

#Mostra um valor aleatorio entre um iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""

#Shuffler() -> Tem a função de embaralhar Dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas)

print(cartas.pop())
