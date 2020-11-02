from processoSimulado import ProcessoSimulado
from tabelaProcessos import TabelaProcessos
from copy import deepcopy

class CPU:
    quantumUsado = 0
    contadorProgramaAtual = 0
    processoExecut = ProcessoSimulado(-1,-1,-1,-1)
    # Alteração do quantum com base na prioridade de cada processo
    quantum = { 0:1, 1:2, 2:4, 3:8 }

    def __init__(self):
        self.quantumUsado = 0
        self.contadorProgramaAtual = 0
        self.processoEmExecucao= ProcessoSimulado(-1,-1,-1,-1)

    def passarQuantum(self):
        self.quantumUsado += 1
        print('\n\n⏲️  Quantum disponível: '+str(self.quantum[self.processoEmExecucao.prioridade]) + ' --- ⏱️  Quantum usado: ' + str(self.quantumUsado))
        if (self.quantumUsado < self.quantum[self.processoEmExecucao.prioridade]):
            return False # Não é necessário incrementar a prioridade
        else:
            print('⚠️  Incrementa a prioridade do processo')
            self.quantumUsado = 0
            return True

    def executarProcesso(self, processoSimulado):
        self.processoEmExecucao = deepcopy(processoSimulado)
        self.contadorProgramaAtual = self.processoEmExecucao.contadorPrograma

    def declararValor(self, processoSimulado, indice):
        processoSimulado.declararValor(indice)

    def somaValor(self, processoSimulado, indice, valor):
        processoSimulado.somaValor(indice, valor)
