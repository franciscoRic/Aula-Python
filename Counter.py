"""

Modulo Collections - Counter


lista = [1, 1, 11, 2, 2, 2, 3, 3, 4, 4, 4, 80, 81, 90, 7, 7, 7, 80, 80, 90, 6, 6, 8, 9]

res = Counter(lista)

print(res)
print(type(res))

print(Counter('Francisco Ricardo'))

"""

from collections import Counter

texto = """ Help Wanted é o episódio piloto da série de televisão animada estadunidense SpongeBob SquarePants, transmitido originalmente nos Estados Unidos em 1º de maio de 1999 através do canal de televisão Nickelodeon após a emissão televisiva da cerimônia de prêmios infantis do mesmo canal. O seu enredo foi escrito por Stephen Hillenburg, que também serviu como diretor e artista de storyboard, Derek Drymon, que igualmente serviu como artista de storyboard, e Tim Hill. A animação, por sua vez, foi dirigida pelo diretor de supervisão da série, Alan Smart. "Help Wanted" apresenta uma performance musical póstuma de Tiny Tim cantando o tema "Livin' in the Sunlight, Lovin' in the Moonlight".

O episódio acompanha o protagonista, uma esponja jovem antropomórfica chamada SpongeBob SquarePants, tentando conseguir um emprego no Krusty Krab, um restaurante local. No entanto, tem a tarefa de encontrar uma espátula mecânica aparentemente rara porque o proprietário, Mr. Krabs, considera-o não qualificado para o cargo. Eventualmente, multidões de anchovas vorazes vão ao Krusty Krab e exigem refeições. SpongeBob retorna de sua missão, tendo cumprido o pedido do Mr. Krabs e encontrado uma espátula mecânica que posteriormente usa para satisfazer a fome das anchovas. Então, contra os desejos do caixa Squidward Tentacles, SpongeBob é recebido por Mr. Krabs como um funcionário do restaurante.

Hillenburg, criador de SpongeBob SquarePants, inicialmente concebeu a série em 1994 e começou a trabalhar nela logo após o cancelamento de Rocko's Modern Life dois anos depois. Para vocalizar SpongeBob, aproximou-se de Tom Kenny, com quem havia trabalhado em Rocko's Modern Life e, para o enredo, originalmente teve a ideia de ter SpongeBob e Squidward em uma viagem, inspirado-se no filme Powwow Highway (1989). Contudo, Hillenburg desistiu e, juntamente com Kenny e Derek Drymon, idealizaram um conceito novo baseado em uma experiência de Hillenburg enquanto membro dos Boy Scouts. A ideia original seria usada posteriormente no episódio "Pizza Delivery", mais tarde na temporada.

Em geral, "Help Wanted" foi recebido com opiniões positivas pelos membros da crítica especialista em televisão animada. Segundo os dados publicados pelo serviço de mediação de audiências Nielsen Ratings, foi assistido por uma média de 6,90 milhões de telespectadores ao longo da sua transmissão original, recebendo a classificação de 3,6 no perfil demográficos dos telespectadores entre os dois aos onze anos de idade. Não obstante, como a Nickelodeon não queria pagar ao patrimônio de Tiny Tim pelos direitos de autor, o episódio foi excluído do lançamento em DVD da primeira temporada de SpongeBob SquarePants. Desde então, foi incluso como um episódio bônus em vários outros DVDs da série.
"""
palavras = texto.split()

#print(palavras)

res = Counter(palavras)

print(res)

#Encontrando as 5 palavras com mais ocorrrencias no texto
print(res.most_common(10))
