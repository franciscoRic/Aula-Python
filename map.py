"""

MAP

import math

def area(r):
    ##Calcula a área de um circulo com o Raio r
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

#forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)


print("---------------------------------------------")

# Forma 2 com Map
## Map é uma função que recebe dois paramentos, o primeiro uma função o segundo um iterável.

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

print("---------------------------------------------")

# Forma 3 lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

#Apos utilizar a função map depois do resultado ele zera os dados na variavel

"""

#Para fixar - Map

#Exemplo

cidade = [('Belim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Yorke', 28), ('Londres', 22)]

print(cidade)

# f = 9/5 * c + 32

#lambida

c_para_f = lambda dados: (dados[0], (9/5 * dados[1] + 32))

print(list(map(c_para_f, cidade)))

