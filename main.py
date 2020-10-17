from gerenciadorProcessos import GerenciadorProcessos
from processoSimulado import ProcessoSimulado

ger = GerenciadorProcessos()
ger.inserirProcesso(ProcessoSimulado(21, 1024, 0, 0, 1))
ger.inserirProcesso(ProcessoSimulado(23, 1024, 0, 0, 2))
ger.inserirProcesso(ProcessoSimulado(2, 1024, 0, 0, 0))
ger.imprimirProcessos(True)
