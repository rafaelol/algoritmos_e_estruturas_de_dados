def subconjunto(conjunto, nivel, marca):
    if nivel == len(conjunto):
        subset = []
        for i in range(0, len(conjunto)):
            if marca[i]:
                subset.append(conjunto[i])
        print subset
    else:
        marca[nivel] = 1
        subconjunto(conjunto, nivel + 1, marca)
        marca[nivel] = 0
        subconjunto(conjunto, nivel + 1, marca)

conjunto = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
marca = [0 for i in range(0, len(conjunto))]
print conjunto
print marca

subconjunto(conjunto, 0, marca)
