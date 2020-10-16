from objects.tabelaProcessos import tabelaProcessos
from objects.processoImpressao import *
from objects.processo import *

class gerenciadorProcessos:
    tempo = 0
    tabelaProcesso = tabelaProcessos.tabelaProcessos()
    estadoExec = 0
    estadoPronto = [] #queue
    estadoBloqueado = [] #queue

    def __init__(self):
        self.tempo = 0

    def inserirBloqueado(self,processo : processo):
        self.estadoBloqueado.append(processo.idProcesso)
        processo.mudarEstadoProcesso(0)

    def inserirPronto(self,processo : processo):
        self.estadoPronto.append(processo.idProcesso)
        processo.mudarEstadoProcesso(1)

    def inserirProcessoExecut(self,processo:processo):
        self.estadoExec = processo.idProcesso
        processo.mudarEstadoProcesso(2)

    def inserirProcesso(self,novoProcesso: processo):
        self.tabelaProcesso.adicionarProceso(novoProcesso)

    def imprimirProcessos(self,modoDetalhado: bool):
        ProcessoImpressao(modoDetalhado,self.tabelaProcesso)
