class TabelaProcessos:
    listaProcessos = []

    def __init__(self):
        self.listaProcessos = []

    def retornaLista(self):
        return self.listaProcessos

    def adicionarProcesso(self, processo):
        self.listaProcessos.append(processo)

    def removerProcesso(self,processo):
        if processo in self.listaProcessos:
            self.listaProcessos.remove(processo)

    def buscarProcesso(self,idProcesso:int):
        for processo in self.listaProcessos:
            if processo.idProcesso == idProcesso:
                return processo
    
    def buscarProcessoIndice(self,idProcesso:int):
        for processo in self.listaProcessos:
            if processo.idProcesso == idProcesso:
                return self.listaProcessos.index(processo)