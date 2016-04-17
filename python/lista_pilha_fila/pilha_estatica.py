class Pilha():
    def __init__(self, tam_max):
        self._pilha = [0 for i in range(0, tam_max)]
        self._tammax = tam_max
        self._topo = 0

    def leia(self):
        if self._topo == 0:
            return None
        return self._pilha[self._topo - 1]
        
    def insere(self, elemento):
        if self._topo == self._tammax:
            return None
        self._pilha[self._topo] = elemento
        self._topo += 1
        return self._topo

    def remove(self):
        if self._topo == 0:
            return None
        self._topo -= 1
        return self._topo

max = int(raw_input('Tamanho maximo da pilha: '))
pilha = Pilha(max)

