from processoSimulado import ProcessoSimulado
from tabelaProcessos import TabelaProcessos
from copy import copy,deepcopy


class CPU:
    quantum = {0:1,1:2,2:4,3:8}
    quantumUsado = 0
    pcAtual = 0
    processoExecut = ProcessoSimulado(-1,-1,-1,-1)


    def __init__(self):
        self.quantumUsado = 0
        self.pcAtual = 0
        self.processoExecut= ProcessoSimulado(-1,-1,-1,-1)

    def passarQuantum(self):
        self.quantumUsado+=1
        self.processoExecut.tempoCPU+=1
        if(self.quantumUsado <= self.quantum[self.processoExecut.prioridade]):
            return False
        self.quantumUsado = 0
        return True 

    def mudarProcesso(self,processo : ProcessoSimulado):
        #COMENTÁRIO PRA ESTELA NÃO ESQUECER
        #QUANDO ACABAR O PROCESSO DEVEMOS RETORNAR TODOS OS VALORES USADOS PELA CPU
        self.processoExecut = copy(processo)
        self.quantumUsado = 0
        self.pcAtual = processo.contadorPrograma

    def executarInstruction(self):
        #Executar processo
        self.quantumUsado+=1
        self.pcAtual+=1


    def declararValor(self,processo: ProcessoSimulado,indice):
        processo.declararValor(indice)

    def somaValor(self,processo:ProcessoSimulado,indice,valor):
        processo.somaValor(indice,valor)
    
