from random import randint

def fill_sorted(size, max):
    lista = [randint(0, max) for i in range(size)]
    lista.sort()
    return lista

def busca_binaria(lista, elemento, inicio, fim):
    if (fim - inicio) == 1:
        if lista[inicio] != elemento:
            return -1
        else:
            return inicio

    meio = (fim + inicio) / 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, fim)
    else:
        return busca_binaria(lista, elemento, inicio, meio)

lista = fill_sorted(10000, 99999)
algum = lista[randint(0, 10000)]
print busca_binaria(lista, algum, 0, len(lista))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print busca_binaria(lista, 0, 0, len(lista))
print busca_binaria(lista, 1, 0, len(lista))
print busca_binaria(lista, 2, 0, len(lista))
print busca_binaria(lista, 3, 0, len(lista))
print busca_binaria(lista, 4, 0, len(lista))
print busca_binaria(lista, 5, 0, len(lista))
print busca_binaria(lista, 6, 0, len(lista))
print busca_binaria(lista, 7, 0, len(lista))
print busca_binaria(lista, 8, 0, len(lista))
print busca_binaria(lista, 9, 0, len(lista))
print busca_binaria(lista, 10, 0, len(lista))
print busca_binaria(lista, 11, 0, len(lista))

