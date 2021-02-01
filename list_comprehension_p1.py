"""
List Comprehension

Gera novas listas com dados processados a partir de outro interável

##Sintaxe

[ dado for dado in interavel ]

##Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


Para entender melhor melhor o que esta acontecendo devemos dividir a expressão em duas partes

- A 1º parte: for numero in numeros
- A 2ª parte: numero * 10


##Função para elevar ao quadrado


def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

##List Comprehension versus loop

#Com loop

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#Com List Comprehension

print([numero * 2 for numero in numeros ])


"""

## 1

nome = 'Francisco Ricardo'

print([letra.upper() for letra in nome])

## 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

## 3

print([numero * 3 for numero in range(1, 10)])

