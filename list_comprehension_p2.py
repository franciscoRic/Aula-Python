"""
List Comprehension

Podemos adicionar estruturas condicionais lógicas as nossas list comprehension

"""

#Exemplo

#1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(numeros)
print(pares)
print(impares)

# Refatorando

#Qualquer numero par módulo de 2 é 0 e o 0 em Python e False. not False = True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


#2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)