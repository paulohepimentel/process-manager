class ProcessoSimulado:
    idProcesso = 0
    idProcessoPai = 0
    contadorPrograma = 0
    valor = []
    instrucoes = []
    tempoInicio = 0
    tempoCPU = 0
    estadoProcesso = 0 # Bloqueado = 0, Pronto = 1, Em execução == 2

    def __init__(self, id, contador, tempoInicio, idPai=0, estadoProcesso=0, valor=1):
        self.idProcesso = id
        self.idProcessoPai = idPai
        self.tempoInicio = tempoInicio
        self.tempoCPU = 0
        self.contadorPrograma = contador
        self.estadoProcesso = estadoProcesso
        self.valor = [0 for i in range(valor)]

    def mudarEstadoProcesso(self, estadoProcesso):
        self.estadoProcesso = estadoProcesso

    def executarProcesso(self):
        self.tempoCPU += 1

    def retornaEstado(self):
        if self.estadoProcesso == 0:
            return "Bloqueado"
        elif self.estadoProcesso == 1:
            return "Pronto"
        elif self.estadoProcesso == 2:
            return "Em Execução"

    def imprimeProcessoDetalhado(self):
        print("-----------------------------------------------------")
        print("idProcesso :"+str(self.idProcesso))
        print("Id do Processo Pai:"+str(self.idProcessoPai))
        print("Estado:"+self.retornaEstado())
        print("Tempo Inicial:"+str(self.tempoInicio))
        print("Tempo de CPU:"+str(self.tempoCPU))
        print("-----------------------------------------------------")

    def imprimeProcessoSimplificado(self):
        print("-----------------------------------------------------")
        print("idProcesso :"+str(self.idProcesso))
        print("Estado:"+self.retornaEstado())
        print("-----------------------------------------------------")
