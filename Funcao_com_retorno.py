"""

Funções com Retorno

numeros = [1, 2, 3]

ret = numeros.pop()

print(ret)
print(numeros)

def quadrado():
    return 7 * 7


print(quadrado())

def outrafuncao():
    return 1, 2, 3, 4


num1, num2, num3, num4 = outrafuncao()

print(num1, num2, num3, num4)
print(outrafuncao())


from random import random


def joaga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joaga_moeda())


"""

