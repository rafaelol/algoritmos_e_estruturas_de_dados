from random import randint
from copy import deepcopy

def fill(size, max):
	return [randint(0, max) for i in range(size)]

def bubble(lista):
	for i in range(0, len(lista)):
		for j in range(0, len(lista) - 1):
			if lista[j] > lista[j + 1]:
				aux = lista[j + 1]
				lista[j + 1] = lista[j]
				lista[j] = aux

	return lista

v1 = fill(20, 100)

print "Original"
print v1
print "Bubble"
print bubble(deepcopy(v1))
