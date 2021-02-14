"""

Len, Abs, Sum e Round

#Dumer Len
print('Francisco Ricardo'.__len__())

#abs() => retorna o valor absoluto de um numero inteiro ou real. Deforma basica, seria o seu valor real sem o sinal
#Retorna sempre um valor positivo

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

#sum() => soma os valor de um iteravel ou dois valores
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

"""
#round() => arrendonda os numeros real para n digitos de precisão.

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.1212512151515, 2))
print(round(1.219999999, 2))
