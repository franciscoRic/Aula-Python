"""
lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""
#Exemplos

numeros = {num for num in range(1, 7)}

print(numeros)

#exemplo 2

numeros1 = {x ** 2 for x in range(10)}

print(numeros1)

#Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set

numeros2 = {x: x ** 2 for x in range(10)}

print(numeros2)

letras = {letra for letra in 'Francisco Ricardo'}
letrass = (letra for letra in 'Francisco Ricardo')
letrasss = [letra for letra in 'Francisco Ricardo']

print(letras)
print(letrass)
print(letrasss)