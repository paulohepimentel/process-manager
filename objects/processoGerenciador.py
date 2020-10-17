import os
from tabelaProcessos import TabelaProcessos
from processoImpressao import ProcessoImpressao
from processoSimulado import ProcessoSimulado

class ProcessoGerenciador:

    def __init__(self):
        self.tempo = 0
        self.estadoExec = 0
        self.estadoPronto = [] #queue
        self.estadoBloqueado = [] #queue
        self.tabelaProcesso = TabelaProcessos()

    def inserirBloqueado(self, processo:ProcessoSimulado):
        self.estadoBloqueado.append(processo.idProcesso)
        processo.mudarEstadoProcesso(0)

    def removerBloqueado(self, processo:ProcessoSimulado):
        self.estadoPronto.insert(self.estadoBloqueado.pop(0))
        processo.mudarEstadoProcesso(1)

    def inserirPronto(self, processo:ProcessoSimulado):
        self.estadoPronto.append(processo.idProcesso)
        processo.mudarEstadoProcesso(1)

    def inserirProcessoExec(self, processo:ProcessoSimulado):
        self.estadoExec = processo.idProcesso
        processo.mudarEstadoProcesso(2)

    def inserirProcessoNaTabela(self, processo:ProcessoSimulado):
        self.tabelaProcesso.adicionarProceso(processo)

    def recebeComandoDoControle(self, comandoRecebido):
        comandoRecebido = comandoRecebido.decode()

        # U: Fim de uma unidade de tempo, enquanto não ocorre o fim, o tempo
        # está parado. O tempo passa quando o comando U é recebido.
        if(comandoRecebido == 'U'):
            print('💧 O gerenciador de processos incrementou o tempo' + '\n')
            #self.tempo += 1

        # L: Desbloqueia o primeiro processo simulado na fila bloqueada.
        elif(comandoRecebido == 'L'): 
            print('💧 O gerenciador de processos desbloqueou o primeiro da fila' + '\n')
            #self.removerBloqueado()

        # I: Imprime o estado atual do sistema.
        elif(comandoRecebido == 'I'):
            print('💧 O gerenciador de processos vai criar o processo impressão' + '\n')
            # Pipe -> file descriptors r para leitura e w para escrita
            r, w = os.pipe() 

            # Cria o processo impressao
            idProcesso = os.fork()

            if idProcesso: 
                # Processo pai: Processo Gerenciador
                os.close(r)
                w = os.fdopen(w, 'w')
                comando = input('Entre com o D para Impressão Detalhada: ')
                w.write(comando)
                w.close()

            else:
                # Processo filho: Processo Impressão
                os.close(w)
                processoImpressao = ProcessoImpressao()
                r = os.fdopen(r, 'r')
                comandoRecebido = r.read()
                print('O processo impressão leu do pipe o comando: ' + comandoRecebido)
                processoImpressao.recebeComandoDoGerenciador(comandoRecebido, self.tabelaProcesso)

        # M: Imprime o tempo médio do ciclo e finaliza o sistema.
        # tempo médio = (soma do tempo de cpu de todos os processos ainda não finalizados) / (todos os processos)
        elif(comandoRecebido == 'M'):
            print('💧 O gerenciador de processos vai imprimir o tempo médio e encerrar o sistema' + '\n')

        else:
            print('💧 O gerenciador de processos não reconhece o comando: ' + comandoRecebido + '\n')