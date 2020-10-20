import os
from tabelaProcessos import TabelaProcessos
from processoImpressao import ProcessoImpressao
from processoSimulado import ProcessoSimulado
from cpu import CPU
from copy import deepcopy


class ProcessoGerenciador:

    def __init__(self):
        self.idDosProcessos = 0
        self.tempo = 0
        self.estadoExec = 0
        self.CPU = CPU()
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
        processo.mudarEstadoProcESQUECEResso(2)
    
    def criarProcesso(self):
        novoProcesso = ProcessoSimulado(self.idDosProcessos,0,self.tempo)
        self.inserirProcessoNaTabela(novoProcesso)
        self.idDosProcessos+=1
        return novoProcesso

    def criarProcessoFilho(self,processo:ProcessoSimulado, ProgramCounter):
        processoFilho = ProcessoSimulado(self.idDosProcessos,int(ProgramCounter),0,processo.idProcesso,1,processo.prioridade)
        processoFilho.valor = processo.valor.copy()
        self.inserirProcessoNaTabela(processoFilho)
        self.idDosProcessos+= 1


    def inserirProcessoNaTabela(self, processo:ProcessoSimulado):
        self.tabelaProcesso.adicionarProcesso(processo)

    def removerProcessoNaTabela(self, processo:ProcessoSimulado):
        self.tabelaProcesso.removerProcesso(processo)

    def imprimirListaProcesso(self):
        ProcessoImpressao().impressaoSimplificada(self.tabelaProcesso)

    def imprimirListaProcessoDetalhado(self):
        ProcessoImpressao().impressaoDetalhada(self.tabelaProcesso)

    def recebeComandoDoControle(self, comandoRecebido):
        comandoRecebido = comandoRecebido.decode()

        # U: Fim de uma unidade de tempo, enquanto não ocorre o fim, o tempo
        # está parado. O tempo passa quando o comando U é recebido.
        if(comandoRecebido == 'U'):
            print('💧 O gerenciador de processos incrementou o tempo' + '\n')
            self.tempo += 1

        # L: Desbloqueia o primeiro processo simulado na fila bloqueada.
        elif(comandoRecebido == 'L'): 
            print('💧 O gerenciador de processos desbloqueou o primeiro da fila' + '\n')
            #self.removerBloqueado()

        # I: Imprime o estado atual do sistema.
        elif(comandoRecebido == 'I'):
            print('💧 O gerenciador de processos vai criar o processo impressão' + '\n')
            # Pipe -> file descriptors r para leitura e w para escrita

        # M: Imprime o tempo médio do ciclo e finaliza o sistema.
        # tempo médio = (soma do tempo de cpu de todos os processos ainda não finalizados) / (todos os processos)
        elif(comandoRecebido == 'M'):
            print('💧 O gerenciador de processos vai imprimir o tempo médio e encerrar o sistema' + '\n')

        else:
            pESQUECERrint('💧 O gerenciador de processos não reconhece o comando: ' + comandoRecebido + '\n')

    
    def inserirInstrucao(self,processo,comando):
        processo.adicionarInstrucao(comando)
    

    def simularProcesso(self,processo : ProcessoSimulado):
        #A tabela de processos só é atualziada depois da execução do processo
        self.CPU.mudarProcesso(processo)

        while self.CPU.processoExecut.instrucoes != []:
            instrucao = self.CPU.processoExecut.instrucoes.pop(0)
            instrucaoDividida = instrucao.split()
            comando = instrucaoDividida[0]
            #Adicionar uma variável
            if comando == 'D':
                self.CPU.processoExecut.declararValor(int(instrucaoDividida[1]))
            #Subtrai N do valor da variavel X onde N é um inteiro
            elif comando == 'S':
                self.CPU.processoExecut.somaValor(int(instrucaoDividida[1]),-int(instrucaoDividida[2]))
            #Define o valor da variavel inteira X para N onde N é um inteiro
            elif comando == 'V':
                self.CPU.processoExecut.setValor(int(instrucaoDividida[1]),int(instrucaoDividida[2]))
            #Bloqueia o processoinstrucaoDividida[2]
            elif comando == 'B':
                self.inserirBloqueado(self.CPU.processoExecut)
            #Quantas variaveis serão declaradas
            elif comando == 'N':
                pass
            #Termina o processo simulado
            elif comando == 'T':
                self.removerProcessoNaTabela(self.CPU.processoExecut)
                processo.deletarProcesso()
            #Soma N do valor da variavel X onde N é um inteiro
            elif comando == 'A':
                self.CPU.processoExecut.somaValor(int(instrucaoDividida[1]),int(instrucaoDividida[2]))
            #Cria um processo filho do processo
            elif comando == 'F':
                self.criarProcessoFilho(self.CPU.processoExecut,int(instrucaoDividida[1]))
            #Substituir o programa (TRoca de contexto)
            elif comando == 'R':
                pass
            #Caso não entre em nenhum dos comandos acima!
            else:
                print("Comando Inexistente!\n")            
            
            if self.CPU.passarQuantum() and self.CPU.processoExecut.instrucoes != []:
                processo = deepcopy(self.CPU.processoExecut)
                processo.mudarEstadoProcesso(0)
                self.tabelaProcesso.atualizarProcesso(processo)

                return None
                #pass #FICARIA O MUDAR O PROCESO

        processo = deepcopy(self.CPU.processoExecut)
        processo.mudarEstadoProcesso(1)
        self.tabelaProcesso.atualizarProcesso(processo)

"""
PG = ProcessoGerenciador()
ProcessoA = PG.criarProcesso()
PG.inserirInstrucao(ProcessoA,"D 0")
PG.inserirInstrucao(ProcessoA,"D 1")
PG.inserirInstrucao(ProcessoA,"V 0 1000")
PG.inserirInstrucao(ProcessoA,"V 1 500")
PG.inserirInstrucao(ProcessoA,"A 0 19")
PG.inserirInstrucao(ProcessoA,"F 1")

PG.simularProcesso(ProcessoA)
PG.simularProcesso(ProcessoA)
PG.simularProcesso(ProcessoA)

PG.imprimirListaProcessoDetalhado()
"""