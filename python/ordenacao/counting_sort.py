from random import randint
from copy import deepcopy

def fill(size, max):
	return [randint(0, max) for i in range(size)]

def counting(lista):
	max_number = max(lista)
	aux = [0 for i in range(0, max_number + 1)]
	final = [0 for i in range(len(lista))]
	
	for i in range(0, len(lista)):
		aux[lista[i]] += 1

	for i in range(1, max_number + 1):
		aux[i] += aux[i - 1]
	
	j = len(lista) - 1
	while j >= 0:
		final[aux[lista[j]] - 1] = lista[j]
		aux[lista[j]] -= 1
		j -= 1

	return final

v1 = fill(20, 100)

print "Original"
print v1
print "Counting"
print counting(deepcopy(v1))
