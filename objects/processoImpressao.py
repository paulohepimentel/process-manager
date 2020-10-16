from objects import tabelaProcessos

class ProcessoImpressao:

    def __init__(self,modoDetalhado: bool,tabelaPrcesso : tabelaProcessos):
        if modoDetalhado:
            self.impressaoDetalhada(tabelaPrcesso)
        else:
            self.impressaoSimplificada(tabelaPrcesso)


    @classmethod #Método da classe
    def impressaoDetalhada(cls,tabelaPrcesso : tabelaProcessos):
        for i in tabelaPrcesso.getLista():
            i.printProcessoDetalhado()
        return None

    @classmethod
    def impressaoSimplificada(cls,tabelaPrcesso : tabelaProcessos):
        for i in tabelaPrcesso.getLista():
            i.printProcessoSimplificado()
        return None