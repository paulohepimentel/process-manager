class processo:
    idProcesso = 0
    idProcessoPai = 0
    contadorPrograma = 0
    valor = []
    estado = 0
    # Bloqueado = 0
    # Pronto = 1
    # Em execução = 2


    def __init__(self,id,contador,idPai = 0,estado = 0,valor = 1):
        self.idProcesso = id
        self.idProcessoPai = idPai
        self.contadorPrograma = contador
        self.estado = estado
        self.valor = [0 for i in range(valor)]

    def mudarEstadoProcesso(self,estado):
        self.estado = estado

