from random import randint

def fill(size, max):
    return [randint(0, max) for i in range(size)]

def maior(lista, inicio):
    if inicio == len(lista) - 1:
        return lista[inicio]

    numero = maior(lista, inicio + 1)
    if lista[inicio] > numero:
        return lista[inicio]
    return numero

lista = fill(999, 100000000)

print maior(lista, 0)
