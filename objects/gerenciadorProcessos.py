from objects.tabelaProcessos import tabelaProcessos
from objects.processo import *

class gerenciadorProcessos:
    tempo = 0
    tabelaProcesso = tabelaProcessos()
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
