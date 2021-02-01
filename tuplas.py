"""

# As tuplas são representadas por um ()
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla1)

print(type(tupla2))

# As Duplas devem ter mais de 1 valor.
#Não é tupla

tupla3 = (4)
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)

print(type(tupla4))


tupla5 = 4,
print(tupla5)

print(type(tupla5))

tupla = tuple(range(11))
print(tupla)

print(type(tupla))

#Desempacotamento de Tupla

tupla = ('Francisco Ricardo', 'Analista de sistemas')

escola, curso = tupla

print(escola)
print(curso)

# Metodos para adição e remoção de elementos nas tuplas não existem, pois são imutavei.


# Na Tupla ´podemos usar Soma, maximo, minimo e tamanho

tupla = (1, 2, 3, 4, 5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de Tuplas
tupla1 = 1, 2, 3
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

#VERIFICAR DETERMINADO ELEMENTO EM UMA TUPLA

tupla = 1, 2, 3,

print(3 in tupla)

#Iterando sobre uma tupla

tupla = 1, 2, 3, 3

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

#Contar elementos em uma tupla
print(tupla.count(3))

escola = tuple('Francisco Ricardo')
print(escola)

print(escola.count('R'))

#Onde usar Tupla

mes = ('Janeiro', 'Fevereiro', 'Março')
semana = ('Segunda', 'Terça', 'Quarta')

mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho')

#Iterar com While
i = 0

while i < len(mes):
    print(mes[i])
    i = i + 1

print(mes[2:5])

"""

