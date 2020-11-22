from prettytable import PrettyTable
class ProcessoImpressao:

    def __init__(self):
        print('\t\t\t🟢🟢🟢 Iniciando o Processo Impressão! 🟢🟢🟢\n')

    def impressaoDetalhada(self, tabelaProcessos):
        if len(tabelaProcessos.retornaLista()) == 0:
            print("\t\tOs processos foram concluídos. A tabela de processos está vazia!")
            return None
        print('📑 Tabela de Processos - Modo Detalhado')
        tabela = PrettyTable(['idProcesso', 'idProcessoPai', 'Prioridade', 'Estado', 'Tempo Inicial', 'TempoCPU'])
        for processo in tabelaProcessos.retornaLista():
            dadosDoProcesso = processo.imprimeProcessoDetalhado()
            tabela.add_row(dadosDoProcesso)
        print(tabela)
        return None

    def impressaoSimplificada(self, tabelaProcessos):
        if len(tabelaProcessos.retornaLista()) == 0:
            print("\t\tOs processos foram concluídos. A tabela de processos está vazia!")
            return None
        print('📑 Tabela de Processos - Modo Simplificado')
        tabela = PrettyTable(['idProcesso', 'Prioridade', 'Estado'])
        for processo in tabelaProcessos.retornaLista():
            dadosDoProcesso = processo.imprimeProcessoSimplificado()
            tabela.add_row(dadosDoProcesso)
        print(tabela)
        return None
