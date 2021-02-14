"""

raise => lança exceções

raise TipoDoError('Menssagem de Error')



"""

#Exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore(True, 'Vermelho')

