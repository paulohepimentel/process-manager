#Alunos: Estela Miranda, João Marcos, Paulo Pimentel

from processoSimulado import ProcessoSimulado
from copy import deepcopy

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
    
    def atualizarProcesso(self,processo:ProcessoSimulado):
        processoAntigo = self.buscarProcessoIndice(processo.idProcesso)
        self.listaProcessos[processoAntigo] = deepcopy(processo)

    def ordenarProcessoBloqueados(self):
        tabelaOrdenada = sorted(self.listaProcessos,key=lambda ProcessoSimulado: ProcessoSimulado.prioridade)
        vetorBloqueado = []
        for i in tabelaOrdenada:
            if i.estadoProcesso == 0:
                vetorBloqueado.append(i.idProcesso)
        return vetorBloqueado

"""
tp = TabelaProcessos()
tp.adicionarProcesso(ProcessoSimulado(1,2,0,0,0,0))
tp.adicionarProcesso(ProcessoSimulado(2,2,0,0,0,3))
tp.adicionarProcesso(ProcessoSimulado(3,2,0,0,0,2))
tp.adicionarProcesso(ProcessoSimulado(4,2,0,0,0,1))
print(tp.ordenarProcessoBloqueados()) 
#for i in tp.listaProcessos:
 #   i.imprimeProcessoDetalhado()
 """