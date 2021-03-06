class ProcessoSimulado:

    idProcesso = 0
    contadorPrograma = 0
    tempoInicio = 0
    idProcessoPai = 0
    estado = 0 # Bloqueado:0, Pronto:1, Em execução:2
    prioridade = 0 # 0,1,2,3 sendo que 3 é a mais baixa e 0 a mais alta
    tempoCPU = 0
    instrucoes = []

    def __init__(self, idProcesso, contadorPrograma, tempoInicio, idPai=0, estado=0, prioridade=0):
        self.idProcesso = idProcesso
        self.contadorPrograma = contadorPrograma
        self.tempoInicio = tempoInicio
        self.idProcessoPai = idPai
        self.estado = estado
        self.prioridade = prioridade
        self.tempoCPU = 0
        self.instrucoes = []

    # * Método relacionado a manipulação do estado do processo    
    def retornaEstado(self):
        if self.estado == 0:
            return "Bloqueado"
        elif self.estado == 1:
            return "Pronto"
        elif self.estado == 2:
            return "Em Execução"

    # * Métodos relacionados a manipulação das prioridades dos processos
    def incrementarPrioridade(self):
        if self.prioridade < 3:
            self.prioridade+=1

    def decrementarPrioridade(self):
        if self.prioridade > 0:
            self.prioridade-=1

# * Métodos relacionados a execução do processo
    def adicionarInstrucao(self, instrucao:str):
        self.instrucoes.append(instrucao)

    def executarProcesso(self):
        self.tempoCPU += 1

# * Métodos relacionados a impressão do processo
    def imprimeProcessoDetalhado(self):
        dadosDoProcesso = []
        dadosDoProcesso.append(self.idProcesso)
        dadosDoProcesso.append(self.idProcessoPai)
        dadosDoProcesso.append(self.prioridade)
        dadosDoProcesso.append(self.retornaEstado())
        dadosDoProcesso.append(self.tempoInicio)
        dadosDoProcesso.append(self.tempoCPU)
        return dadosDoProcesso

    def imprimeProcessoSimplificado(self):
        dadosDoProcesso = []
        dadosDoProcesso.append(self.idProcesso)
        dadosDoProcesso.append(self.prioridade)
        dadosDoProcesso.append(self.retornaEstado())
        return dadosDoProcesso
