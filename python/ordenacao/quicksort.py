from random import randint
from copy import deepcopy

def fill(size, max):
	return [randint(0, max) for i in range(size)]

def quicksort(lista, inicio, fim):
	if fim > inicio:
		pivot = pivoteia(lista, inicio, fim)
		quicksort(lista, inicio, pivot - 1)
		quicksort(lista, pivot + 1, fim)
	return lista

def pivoteia(lista, inicio, fim):
	i = inicio
	for j in range (inicio + 1, fim + 1):
		if lista[j] < lista[inicio]:
			i += 1
			lista[i], lista[j] = lista[j], lista[i]
	lista[i], lista[inicio] = lista[inicio], lista[i]

	return i

v1 = fill(20, 100)

print "Original"
print v1
print "Quicksort"
print quicksort(deepcopy(v1), 0, 19)
