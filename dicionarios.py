"""

Dicionarios
OBs: Dicionários são conhecidos por Mapas em outras linguagem

Dicionários são coleções do tipo chaves/valor


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

print(pais)
print(type(pais))

#Acessando elementos

print(paises['eua'])

print(paises.get('br'))

#O tipo None em Python sempre retornará falso

receita = {'Jan': 1800, 'fev': 1200, 'Mar': 3000}

print(receita)
print(type(receita))

receita['abr'] = 3500

print(receita)

rec_novo = {'Mai': 2500}

receita.update(rec_novo)

print(receita)

receita.update({'Mai': 3200})

print(receita)

#Remover elementos de um Dicionário

receita = {'Jan': 1800, 'fev': 1200, 'Mar': 3000, 'abr': 3500, 'Mai': 2500}

print(receita)

receita.pop('Mar')

print(receita)

del receita['Mai']

print(receita)

carrinho = []

produto1 = {'nome': 'Playstation', 'Qtd': 1, 'Valor': 2300}
produto2 = {'nome': 'Fifa2020', 'Qtd': 1, 'Valor': 280}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Limpar o Dicionario

print(dir({}))

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

#copy
novo = d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)


"""


