class Fila():
    def __init__(self, tam_max):
        self._fila = [0 for i in range(0, tam_max)]
        self._max = tam_max
        self._inicio = 0
        self._fim = 0
    
    def _lista_vazia(self):
        if self._inicio == self._fim:
            return True
        return False

    def _lista_cheia(self):
        if ((self._inicio % self._max) == (self._fim % self._max)) and self._inicio != self._fim:
            return True
        return False

    def leia(self):
        if self._lista_vazia():
            return None
        return self._fila[(self._inicio % self._max)]
        
    def insere(self, elemento):
        if self._lista_cheia():
            return None
        
        self._fila[self._fim % self._max] = elemento
        self._fim += 1
        return elemento

    def remove(self):
        if self._lista_vazia():
            return None
        valor = self._fila[self._inicio % self._max]
        self._inicio += 1
        if self._inicio == self._fim:
            self._inicio, self._fim = 0, 0
        return valor

max = int(raw_input('Tamanho maximo da fila: '))
fila = Fila(max)

