"""

Entendo os *args

# Exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(1, 2, 3))

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

ou


"""
# Entendendo o *args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(4, 5, 6))
print(soma_todos_numeros(7, 8, 9, 10))

