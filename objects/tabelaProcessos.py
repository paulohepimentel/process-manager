from objects.processo import *

class tabelaProcessos:
    listaProcessos = []

    def __init__(self):
        self.listaProcessos = []

    def adicionarProceso(self,processo,tempoInicio,prioridade,tempoCPU=0):
        self.listaProcessos.append([processo,tempoInicio,prioridade,tempoCPU])