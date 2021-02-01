"""

Collections -> Named Tuple

tupla = (1, 2, 3)

print(tupla[1])

Named significa nomeada
Named Tuple -> São tupla, diferenciadas, voce pode criar um tipo de dado seu próprio

"""

from collections import namedtuple

#Precisamos definir o nome e os Parâmetros

#Forma 1 - Declaração da Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2 - Declaração da Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3 - Declaração da Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando


ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

#Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

#Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Ray'))

print(ray.count('Ray'))
