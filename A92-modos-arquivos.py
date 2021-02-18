"""

r -> Abre para leitura - Padrão
w -> Abre para escrita - Sobreescreve o arquivo caso exista
x -> Abre para escrita somente se o arquivo não existir
a -> Append, abre o arquivo para adicionar o conteudo ao final do arquivo, se o arquivo não existir ele criar.

try:
    with open('A92-Universit.txt', 'x') as arquivo:
        arquivo.write('Teste de Conteudo. \n')
except FileExistsError:
    print('Arquivo ja existe')

with open('A92-frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou sair: ')
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta + '\n')
"""


