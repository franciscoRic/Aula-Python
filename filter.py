"""
Filter

filter() - Filtra os dados de uma determinada coleção.

#Biblioteca para trabalhar com dados estatisticos

import statistics

#Dados coletado de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

#OBS: assim como a função Map, a filter recebe dois parametros, sendo uma função e um iteravel


res = filter(lambda x: x > media, dados)

print(media)
print(list(res))

#A Diferença entre map() e filter() e´:

#map() -> Recebe dois paramentrosm uma função e um iteravel, e retorna um objeto mapeando a função para cada elemento do iteravel

#filter() -> Recebe dois paramentrosm uma função e um iteravel, e retorna um objeto filtrando os elementos de acordo com a função

#Exemplo mais complexo

usuarios = [
    {'username': 'samuel', "tweets": ['Eu adoro bolo', 'Eu adoro pizzas']},
    {'username': 'carla', "tweets": ['Eu amo meu gato']},
    {'username': 'jeff', "tweets": []},
    {'username': 'bob123', "tweets": []},
    {'username': 'dogo', "tweets": ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', "tweets": []}
]

print(usuarios)

#Tarefas Filtrar os usuarios que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

print(inativos)

"""

#Combina filter() e map()
from builtins import print

nomes = ['Vanessa', 'Ana', 'Maria', 'Gabriela']

#Devemos criar uma lista contendo, 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda n: f'Sua instrutora é {n}', filter(lambda no: len(no) > 5, nomes)))

print(lista)