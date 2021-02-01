"""

Conjuntos - Referência a teoría dos conjuntos em Matématica

#Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

#Forma 2

s = set({1, 2, 3, 4, 5, 5})

print(s)
print(type(s))


s1 = {1, 'b', True, 34.22, 44}

print(s1)
print(type(s1))

#Usos interessantes com sets

#Adicionar Elementos em conjuntos

s = {1, 2, 3}

print(s)

s.add(4)

print(s)

#Remover Elementos em conjuntos

s = {1, 2, 3}

#Forma 1
print(s)

s.remove(1)

print(s)

#Forma 2
print(s)

s.discard(3)

print(s)

#Copiando um Conjunto para outro

s = {1, 2, 4, 5}

print(s)

#Forma 1 Deep Copy

novo = s.copy()

print(novo)

novo.add(3)

print(novo)

#Forma 2 Shalow Copy

novo = s

print(novo)

novo.add(3)

print(novo)
print(s)

s.clear()

print(s)

# Unir Conjuntos

a = {1, 2, 3, 4}
b = {3, 5, 6, 7, 8}

#Forma1 - Union

print(a)
print(b)

c = a.union(b)

print(c)

c.add(11)
#Forma 2 Pipe |

d = a | b | c

print(d)

#Elementos que estão em ambos conjuntos

#Forma 1 - Intersecion

e = {1, 2, 3, 4}
f = {3, 5, 6, 7, 8}

g = e.intersection(f)

print(g)

#Forma 2 - Usando &

h = e & f

print(h)

#Conjuntos de elementos distintos

i = {1, 2, 3, 4}
j = {3, 5, 6, 7, 8}

k = i.difference(j)
l = j.difference(i)

print(k)
print(l)

"""


#Soma, Max, Min e Len

m = {3, 5, 6, 7, 8}

print(sum(m))
print(max(m))
print(min(m))
print(len(m))