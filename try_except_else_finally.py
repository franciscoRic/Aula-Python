"""

Try, Except, Else e Finally

try:
    num = int(input('Insira um numero: '))
except ValueError:
    print('Digite apenas numeros')
else: ##Somente é executado se não ocorrer o error.
    print(f'Voce digitou {num}')


"""

try:
    num = int(input('Insira um numero: '))
except ValueError:
    print('Digite apenas numeros')
else:
    print(f'Voce digitou {num}')
finally: ## O bloco finally sempre e executao, mesmo havendo exceção ou não
    print(f'Executando o Finally')




