"""
Reduce

A partir do python3 a função reduce() não é mais uma função integrada (built-in). Agora teremos que importar e utilizar esta função a partir do módulo 'functools'



"""

from functools import reduce

# Utilizando reduce() para multiplicar os valores de uma lista

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando loop for

res1 = 1
for n in dados:
    res1 = res1 * n

print(res)