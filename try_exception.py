"""
Try/Exception

#Tratando um error Genérico
try:
    geek()
except:
    print('Deu algum problema')

#Tratando um error expecifico

try:
    len(5)
except TypeError:
    print('Deu algum problema')


try:
    len(5)
except TypeError as err:
    print(f'Deu algum problema, erro: {err}')


try:
    len(5)
except NameError as erra:
    print(f'Deu NameError, erro: {erra}')
except TypeError as errb:
    print(f'Deu TypeError, erro: {errb}')

try:
    geek()
except NameError as erra:
    print(f'Deu NameError, erro: {erra}')
except TypeError as errb:
    print(f'Deu TypeError, erro: {errb}')


"""

def pe_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'francisco'}

print(pe_valor(dic, 'nome'))
