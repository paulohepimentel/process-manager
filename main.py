
from objects.tabelaProcessos import *

procs = processo(21,1024,0,1)
tabela = tabelaProcessos()
tabela.adicionarProceso(processo,1,0)
print(tabela.listaProcessos[0][0])
