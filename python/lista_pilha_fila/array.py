class Vetor():
    def __init__(self, tam_max):
        self._vetor = [0 for i in range(0, tam_max)]
        self._tammax = tam_max
        self._tamanho = 0

    def busca(self, elemento):
        for i in range(0, self._tamanho):
            if self._vetor[i] == elemento:
                return i

        return None

    def leia(self, pos):
        if pos < self._tamanho:
            return self._vetor[pos]
        return None

    def insere(self, elemento):
        if self._tamanho >= self._tammax:
            return None
        pos_elemento = self.busca(elemento)
        if pos_elemento is None:
            pos_elemento = self._tamanho
            self._vetor[self._tamanho] = elemento
            self._tamanho += 1
        return pos_elemento
        
    def remove(self, elemento):
        if self._tamanho == 0:
            return None
        pos_elemento = self.busca(elemento)
        if pos_elemento is None:
            return None
        for i in range(pos_elemento, self._tamanho - 1):
            self._vetor[i] = self._vetor[i + 1]
        self._tamanho -= 1
        return pos_elemento

max = int(raw_input('Tamanho maximo do vetor: '))
vetor = Vetor(max)

