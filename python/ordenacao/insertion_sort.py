from random import randint
from copy import deepcopy

def fill(size, max):
	return [randint(0, max) for i in range(size)]

def insertion(lista):
	for i in range(0, len(lista)):
		valor = lista[i]
		j = i - 1
		while (j >= 0 and lista[j] > valor):
			lista[j + 1] = lista[j]
			j = j - 1	
		lista[j + 1] = valor

	return lista

v1 = fill(20, 100)

print "Original"
print v1
print "Insertion"
print insertion(deepcopy(v1))
