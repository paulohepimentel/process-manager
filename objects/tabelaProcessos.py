from processoSimulado import ProcessoSimulado
from copy import deepcopy
from operator import attrgetter

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

    def ordenarNumeroInstrucoes(self):
        tabelaOrdenada = sorted(self.listaProcessos,key=lambda ProcessoSimulado: ProcessoSimulado.instrucoes)
        vetorBloqueado = []
        for i in tabelaOrdenada:
            if i.estadoProcesso == 0:
                vetorBloqueado.append(i.idProcesso)
        return vetorBloqueado

tp = TabelaProcessos()
processo = ProcessoSimulado(18,2,0,0,0,0)
processo.adicionarInstrucao("INSTRUCTION")
processo.adicionarInstrucao("INSTRUCTION")
processo.adicionarInstrucao("INSTRUCTION")
processo2 = ProcessoSimulado(13,2,0,0,0,0)
processo2.adicionarInstrucao("INSTRUCTION")
processo2.adicionarInstrucao("INSTRUCTION")
tp.adicionarProcesso(processo)
tp.adicionarProcesso(processo2)

tp.adicionarProcesso(ProcessoSimulado(2,2,0,0,0,3))
tp.adicionarProcesso(ProcessoSimulado(3,2,0,0,0,2))
tp.adicionarProcesso(ProcessoSimulado(4,2,0,0,0,1))
print(tp.ordenarNumeroInstrucoes()) 
#for i in tp.listaProcessos:
 #   i.imprimeProcessoDetalhado()