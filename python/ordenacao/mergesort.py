from random import randint
from copy import deepcopy

def fill(size, max):
    return [randint(0, max) for i in range(size)]

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) / 2
        return merge(mergesort(lista[:meio]), mergesort(lista[meio:]))

    return lista
    
def merge(lista_esquerda, lista_direita):
    if len(lista_esquerda) == 0:
        return lista_direita
    elif len(lista_direita) == 0:
        return lista_esquerda
    else:
        if lista_esquerda[0] < lista_direita[0]:
            return [lista_esquerda[0]] + merge(lista_esquerda[1:],lista_direita)
        else:
            return [lista_direita[0]] + merge(lista_esquerda,lista_direita[1:])
 

v1 = fill(20, 100)

print "Original"
print v1
print "Mergesort"
print mergesort(deepcopy(v1))
