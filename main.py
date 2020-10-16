from objects.gerenciadorProcessos import *
ger = gerenciadorProcessos()
ger.inserirProcesso(processo(21,1024,0,0,1))
ger.inserirProcesso(processo(23,1024,0,0,2))
ger.inserirProcesso(processo(2,1024,0,0,0))
ger.imprimirProcessos(True)
