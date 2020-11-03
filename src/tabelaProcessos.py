from processoSimulado import ProcessoSimulado
from copy import deepcopy

class TabelaProcessos:
    listaProcessos = []

    def __init__(self):
        self.listaProcessos = []

    # * CRUD de processos na estrutura Tabela de Processos
    def retornaLista(self):
        return self.listaProcessos

    def adicionarProcesso(self, processo):
        self.listaProcessos.append(processo)

    def removerProcesso(self, processo):
        id = processo.idProcesso
        for processo in self.listaProcessos:
            if processo.idProcesso == id:
                self.listaProcessos.remove(processo)
                break

    def atualizarProcesso(self, processoSimulado):
        for processo in self.listaProcessos:
            if processo.idProcesso == processoSimulado.idProcesso:
                processoAntigo = self.listaProcessos.index(processo)
                break

        self.listaProcessos[processoAntigo] = deepcopy(processoSimulado)

    def atualizarEstadoProcessoPorIndice(self, idProcesso, estado):
        for processo in self.listaProcessos:
            if processo.idProcesso == idProcesso:
                processoAntigo = processo
                processoAntigoIndice = self.listaProcessos.index(processo)
                break

        processoAntigo.estado = estado
        self.listaProcessos[processoAntigoIndice] = deepcopy(processoAntigo)


    # * Método relacionado a busca de processos na Tabela de Processos
    def buscarProcesso(self, idProcesso:int):
        for processo in self.listaProcessos:
            if processo.idProcesso == idProcesso:
                return processo

    def defineProcessoEmExecucao(self, processoSimulado):
        for processo in self.listaProcessos:
            if processo.idProcesso != processoSimulado.idProcesso and processo.estado == 2:
                processoAntigo = processo
                processoAntigoIndice = self.listaProcessos.index(processo)
                processoAntigo.estado = 1 # Pronto
                self.listaProcessos[processoAntigoIndice] = deepcopy(processoAntigo)

    # * Métodos relacionados a ordenação de processos na Tabela de Processos
    def ordenarProcessosBloqueados(self):
        tabelaOrdenada = sorted(self.listaProcessos, key=lambda ProcessoSimulado:ProcessoSimulado.prioridade)
        vetorBloqueado = []
        for i in tabelaOrdenada:
            if i.estado == 0:
                vetorBloqueado.append(i.idProcesso)
        return vetorBloqueado

    def ordenarProcessosProntos(self):
        tabelaOrdenada = sorted(self.listaProcessos, key=lambda ProcessoSimulado: ProcessoSimulado.prioridade)
        vetorPronto = []
        for i in tabelaOrdenada:
            if i.estado == 2 or i.estado == 1:
                vetorPronto.append(i.idProcesso)
        return vetorPronto

    def ordenarNumeroInstrucoes(self):
        tabelaOrdenada = sorted(self.listaProcessos, key=lambda ProcessoSimulado: ProcessoSimulado.instrucoes)
        vetorBloqueado = []
        for i in tabelaOrdenada:
            if i.estado == 2 or i.estado == 1:
                vetorBloqueado.append(i.idProcesso)
        return vetorBloqueado
