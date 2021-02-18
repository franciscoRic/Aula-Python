"""
Leitura de arquivos

Seek() -> Usado para movimentar o cursor pelo arquivo

print(arquivo.read())

arquivo.seek(10)

print('######################')

print(arquivo.read())

#ReadLine() -> Ler o arquivo linha a linha

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

ret = arquivo.readline()

print(type(ret))

print(ret.split(' '))

##readLines() -> Ler as linhas

linhas = arquivo.readlines()
print(linhas)

print(len(linhas))

"""

arquivo = open('A89-arq1.txt')

print(arquivo.read(20)) ## Ler apenas os 20 caracteres iniciais do arquivo

print(arquivo.closed) ## Verifica se o arquivo está fechado

print(arquivo.close()) ## Fecha o arquivo

print(arquivo.closed)

