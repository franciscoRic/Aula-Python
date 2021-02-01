"""

Collections -> Deque

Deque seria uma lista de alta performance

"""

from collections import deque

deq = deque('Francisco')

print(deq)

#Adicionando elementos no Deque

deq.append('y')

print(deq)

deq.appendleft('k')

print(deq)

# Removendo elementos

print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)
