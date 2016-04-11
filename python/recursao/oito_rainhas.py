def pode_colocar(posicoes, coluna, candidato):
    if coluna == 1:
        return True
    for i in range(1, coluna):
        if (posicoes[i] == candidato):
            return False
        if (abs(posicoes[i] - candidato) == abs(i - coluna)):
            return False
    return True

def oito_rainhas(posicoes, coluna):
    if coluna == 9:
        print posicoes[1:]
        return
    for i in range(1, 9):
        if pode_colocar(posicoes, coluna, i):
            posicoes[coluna] = i
            oito_rainhas(posicoes, coluna + 1)
        
posicoes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
oito_rainhas(posicoes, 1)
