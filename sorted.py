"""

Sorted


#Exemplo
numeros = (6, 1, 8, 2)

print(numeros)

print(sorted(numeros)) # Ordena do menor para o maior

print(numeros)

#Adicionando parametros ao sorted

numeros1 = [6, 1, 8, 2]

print(numeros1)

print(sorted(numeros1))

print(sorted(numeros1, reverse=True))


"""

usuarios = [
    {'username': 'samuel', "tweets": ['Eu adoro bolo', 'Eu adoro pizzas']},
    {'username': 'carla', "tweets": ['Eu amo meu gato']},
    {'username': 'jeff', "tweets": []},
    {'username': 'bob123', "tweets": []},
    {'username': 'dogo', "tweets": ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', "tweets": []}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuarios: usuarios["username"]))

print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
