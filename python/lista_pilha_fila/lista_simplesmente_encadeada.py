class no():
    def __init__(self, valor):
        self._valor = valor
        self._proximo = None

    def set_proximo(self, proximo):
        self._proximo = proximo

    def get_proximo(self):
        return self._proximo

    def get_valor(self):
        return self._valor

class lse(): #lista simplesmente encadeada
    def __init__(self):
        self._no_cabeca = no(None)

    def _percorre(self, valor):
        ant = self._no_cabeca
        prox = self._no_cabeca.get_proximo()

        while prox:
            if prox.get_valor() > valor:
                break
            ant = ant.get_proximo()
            proximo = proximo.get_proximo()    

        return ant, prox

    def imprime_lista(self):
        no = self._no_cabeca.get_proximo()
        while no:
            print no.get_valor()

    def busca(self, valor):
        no = self._no_cabeca.get_proximo()
        while no:
            if no.get_valor() == valor:
                break
            no = no.get_proximo()
        return no

    def insere(self, no):
        ant, prox = self._percorre(no.get_valor())
        no.set_proximo(prox)
        ant.set_proximo(no)

        return no

    def remove(self, no):
        ant, prox = self._percorre(no.get_valor())
        ant.set_proximo(prox.get_proximo())
        prox.set_proximo(None)

        return prox


lista = lse()

for i in range(5, 10):
    nozinho = no(i)
    lista.insere(no)

nozinho = no(25)
lista.insere(no)
nozinho = no(20)
lista.insere(no)
nozinho = no(1)
lista.insere(no)
print lista.imprime_lista()

