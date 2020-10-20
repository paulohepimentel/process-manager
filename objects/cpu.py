from processoSimulado import ProcessoSimulado
from tabelaProcessos import TabelaProcessos


class CPU:
    quantum = {0:1,1:2,2:4,3:8}
    quantumUsado = 0
    pcAtual = 0


    def __init__(self):
        self.quantumUsado = 0
        self.pcAtual = 0

    def passarQuantum(self,prioridade):
        self.quantumUsado+=1
        if(self.quantumUsado <= self.quantum[prioridade]):
            return False
        self.quantumUsado = 0
        return True 


