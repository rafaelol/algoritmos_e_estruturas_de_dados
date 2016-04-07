from random import randint
from copy import deepcopy

INT_MAX = 1000
FIM_HEAP = 0

def fill(size, max):
    return [randint(0, max) for i in range(size)]

def pai(no):
    return no / 2

def filho_esq(no):
    return 2 * no

def filho_dir(no):
    return 2 * no + 1

def upheap(heap, k):
    v = heap[k]
    heap[0] = INT_MAX
    while (heap[pai(k)] <= v):
        heap[k] = heap[pai(k)]
        k = pai(k)
    heap[k] = v

def downheap(heap, k):
    v = heap[k]
    fim_heap = len(heap) - 1
    while (k <= pai(fim_heap)):
        j = filho_esq(k)
        if (filho_esq(k) < fim_heap and heap[filho_esq(k)] < heap[filho_dir(k)]):
            j = filho_dir(k)
        if v >= heap[j]:
            break
        heap[k] = heap[j]
        k = j
    heap[k] = v


def insert(heap, valor):
    heap.append(valor)
    upheap(heap, len(heap) - 1)


def remove(heap):
    if len(heap) <= 1:
        return None
    if len(heap) == 2:
        return heap.pop()

    v = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    downheap(heap, 1)
    return v

def bulk_insert(heap, lista_valores):
    for valor in lista_valores:
        insert(heap, valor)

def bulk_remove(heap):
    saida = []
    while(True):
        v = remove(heap)
        if not v:
            break
        saida.append(v)

    return saida

def heapsort(heap, lista):
    bulk_insert(heap, lista)
    return bulk_remove(heap)


heap = [INT_MAX]
lista = fill(20, 100)

print lista
print heapsort(heap, lista)
