class ProcessoSimulado:
    idProcesso = 0
    idProcessoPai = 0
    contadorPrograma = 0
    valor = []
    instrucoes = []
    tempoInicio = 0
    tempoCPU = 0
    estadoProcesso = 0 # Bloqueado = 0, Pronto = 1, Em execução = 2 
    prioridade = 0 # 0,1,2,3 sendo que 3 é a mais baixa e 0 a mais alta 

    def __init__(self, id, contador, tempoInicio, idPai=0, estadoProcesso=0, prioridade=0):
        self.idProcesso = id
        self.idProcessoPai = idPai
        self.tempoInicio = tempoInicio
        self.tempoCPU = 0
        self.contadorPrograma = contador
        self.estadoProcesso = estadoProcesso
        self.instrucoes = []
        self.valor = {}
        self.prioridade = prioridade 

    def deletarProcesso(self):
        self = None

    def mudarEstadoProcesso(self, estadoProcesso):
        self.estadoProcesso = estadoProcesso

    def executarProcesso(self):
        self.tempoCPU += 1
    
    def declararValor(self,indice):
        self.valor[indice] = 0

    def setValor(self,indice,valor):
        self.valor[indice] = valor
        
    def getValor(self,indice):
        return self.valor[indice]

    def somaValor(self,indice,valor):
        antigoValor = self.getValor(indice)
        novoValor = int(antigoValor)+valor
        self.setValor(indice,novoValor)

    def retornaEstado(self):
        if self.estadoProcesso == 0:
            return "Bloqueado"
        elif self.estadoProcesso == 1:
            return "Pronto"
        elif self.estadoProcesso == 2:
            return "Em Execução"
    
    def adicionarInstrucao(self,instrucao : str):
        self.instrucoes.append(instrucao)

    def incrementarPrioridades(self):
        if self.prioridade == 3:
            return None
        self.prioridade+=1

    def decrementarPrioridades(self):
        if self.prioridade == 0:
            return None
        self.prioridade-=1


    def imprimeProcessoDetalhado(self):
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (str(self.idProcesso), str(self.idProcessoPai), self.retornaEstado(), str(self.tempoInicio), str(self.tempoCPU) +"\t\t"+str(self.valor)))
        print("---------------------------------------------------------------------------------------------------")

    def imprimeProcessoSimplificado(self):
        print("%s\t\t%s" % (str(self.idProcesso), str(self.retornaEstado())))
        print("--------------------------------------------")