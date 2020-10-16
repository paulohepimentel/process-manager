from objects.processo import *

class tabelaProcessos:
    listaProcessos = []

    def __init__(self):
        self.listaProcessos = []

    def getLista(self):
        return self.listaProcessos

    def adicionarProceso(self,processo):
        self.listaProcessos.append(processo)

