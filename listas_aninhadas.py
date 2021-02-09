"""

- Unidirecionais (arrays / vetores);
- Multidimensionais (Matrizes)

Em python temos as listas

numeros = [1, 2, 3, 4, 5]

##Exemplo

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)

print(type(listas))

## Como fazemos para acessar os dados

print(listas[0][1])

print(listas[2][1])

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterando com loops em uma lista aninhada

for list in listas:
    for num in list:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# outros exemplos
# Geramdp um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

#Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores inicias

print([['*' for i in range(1, 4)] for j in range(1, 4)])