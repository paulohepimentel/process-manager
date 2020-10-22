from tabelaProcessos import TabelaProcessos

class ProcessoImpressao:

    @classmethod #Método da classe
    def impressaoDetalhada(cls, tabelaProcessos:TabelaProcessos):
        if len(tabelaProcessos.retornaLista()) == 0:
            print("A lista está vazia! \n")
            return None
        for processo in tabelaProcessos.retornaLista():
            processo.imprimeProcessoDetalhado()
        return None

    @classmethod  #Método da classe
    def impressaoSimplificada(cls, tabelaProcessos:TabelaProcessos):
        if len(tabelaProcessos.retornaLista()) == 0:
            print("A lista está vazia! \n")
            return None
        for processo in tabelaProcessos.retornaLista():
            processo.imprimeProcessoSimplificado()
        return None

    @classmethod  #Método da classe
    def recebeComandoDoGerenciador(cls, comandoRecebido:str, tabelaProcessos:TabelaProcessos):
        if (comandoRecebido == 'D'):
            impressaoDetalhada(tabelaProcessos)
        else:
            impressaoSimplificada(tabelaProcessos)
        return None
