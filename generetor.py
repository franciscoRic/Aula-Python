"""

Generetors

-Tuple Comprehension são chamdas de generetors
print(any(['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel'])

#Utilizando Generetors

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(any(nome[0] == 'C' for nome in nomes))

#Qual a utilidade de getsizeof : => Retorna a quantidade de bytes em memporia do elemento passado como parâmetro
from sys import getsizeof

#Mostra quantos byes a string esta ocupando em memoria
print(getsizeof('Geek'))
print(getsizeof('Francisco'))
print(getsizeof('Francisco Ricardo'))
print(getsizeof(25989866454))
print(getsizeof(True))


from sys import getsizeof

#Gerando uma lista de numeros com list comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dic_comp = getsizeof({x: x * 10 for x in range(1000)})

gen_list = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa, gastamos em memoria:')
print(f'List Comprehension: {list_comp}')
print(f'set Comprehension: {set_comp}')
print(f'Dic Comprehension: {dic_comp}')
print(f'Gen Comprehension: {gen_list}')

"""

# Interando no Generators

gen = (x * 10 for x in range(1000))

print(gen)
print(type(gen))

for num in gen:
    print(num)