class processo:
    idProcesso = 0
    idProcessoPai = 0
    contadorPrograma = 0
    valor = []
    tempoInicio = 0
    tempoCPU = 0
    estado = 0
    # Bloqueado = 0
    # Pronto = 1
    # Em execução = 2


    def __init__(self,id,contador,tempoInicio,idPai = 0,estado = 0,valor = 1):
        self.idProcesso = id
        self.idProcessoPai = idPai
        self.tempoInicio = tempoInicio
        self.tempoCPU = 0
        self.contadorPrograma = contador
        self.estado = estado
        self.valor = [0 for i in range(valor)]

    def mudarEstadoProcesso(self,estado):
        self.estado = estado

    def executarProcesso(self):
        self.tempoCPU+= 1

    def getEstado(self):
        if self.estado == 0:
            return "Bloqueado"
        if self.estado == 1:
            return "Pronto"
        if self.estado == 2:
            return "Em Execução"

    def printProcessoDetalhado(self):
        print("-----------------------------------------------------")
        print("idProcesso :"+str(self.idProcesso))
        print("Id do Processo Pai:"+str(self.idProcessoPai))
        print("Estado:"+self.getEstado())
        print("Tempo Inicial:"+str(self.tempoInicio))
        print("Tempo de CPU:"+str(self.tempoCPU))
        print("-----------------------------------------------------")


    def printProcessoSimplificado(self):
        print("-----------------------------------------------------")
        print("idProcesso :"+str(self.idProcesso))
        print("Estado:"+self.getEstado())
        print("-----------------------------------------------------")


