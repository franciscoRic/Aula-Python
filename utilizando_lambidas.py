"""

Lambidas são funções em nome - funções anônimas

#lambida

lambda x: 3 * x + 1

#Como utilizar a expressão lambida

calc = lambda x: 3 * x + 1

print(calc(4))

# Expressão Lambida com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('Francisco', 'Ricardo'))

print(nome_completo('    FRANCISCO ', '  Ricardo '))

#lambidas sem entrada

amar = lambda : 'Como não amar Python? '

uma  = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)


print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

autores = ['Francisco Ricardo', 'Daniel Neto', 'Joel Filho', 'Carolinie R. Betesek', 'A. C. Souza', 'Danielle Rufino Alves']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

#Função Quadratica
# f(x) = a * x ** 2 + b * x + c

#Definindo a Função

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
