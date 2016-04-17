def permutacao(texto, nivel, marca, candidato):
    if (nivel == len(texto)):
        print ''.join(candidato)
    else:
        for i in range(0, len(texto)):
            if marca[i] == 0:
                candidato[nivel] = texto[i]
                marca[i] = 1
                permutacao(texto, nivel + 1, marca, candidato)
                marca[i] = 0

texto = list("abcd")
candidato = list("abcd")
marca = [0 for i in range(0, len(texto))]

permutacao(texto, 0, marca, candidato)
