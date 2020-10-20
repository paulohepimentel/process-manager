import os
from tabelaProcessos import TabelaProcessos
from processoImpressao import ProcessoImpressao
from processoSimulado import ProcessoSimulado
from cpu import CPU


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
        processo.mudarEstadoProcesso(2)
    
    def criarProcesso(self):
        novoProcesso = ProcessoSimulado(self.idDosProcessos,0,self.tempo)
        self.inserirProcessoNaTabela(novoProcesso)
        self.idDosProcessos+=1
        return novoProcesso

    def criarProcessoFilho(self,processo:ProcessoSimulado):
        processoFilho = ProcessoSimulado(self.idDosProcessos,0,0,processo.idProcesso)
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
            #self.tempo += 1

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
            print('💧 O gerenciador de processos não reconhece o comando: ' + comandoRecebido + '\n')

    
    def inserirInstrucao(self,processo,comando):
        processo.adicionarInstrucao(comando)
    

    def simularProcesso(self,processo : ProcessoSimulado):
        for instrucao in processo.instrucoes:
            instrucaoDividida = instrucao.split()
            comando = instrucaoDividida[0]
            #Adicionar uma variável
            if comando == 'D':
                processo.declararValor(instrucaoDividida[1])
            #Subtrai N do valor da variavel X onde N é um inteiro
            elif comando == 'S':
                processo.somaValor(instrucaoDividida[1],-instrucaoDividida[2])
            #Define o valor da variavel inteira X para N onde N é um inteiro
            elif comando == 'V':
                processo.setValor(instrucaoDividida[1],instrucaoDividida[2])
            #Bloqueia o processo
            elif comando == 'B':
                self.inserirBloqueado(processo)
            #Quantas variaveis serão declaradas
            elif comando == 'N':
                pass
            #Termina o processo simulado
            elif comando == 'T':
                self.removerProcessoNaTabela(processo)
                processo.deletarProcesso()
            #Soma N do valor da variavel X onde N é um inteiro
            elif comando == 'A':
                processo.somaValor(instrucaoDividida[1],instrucaoDividida[2])
            #Cria um processo filho do processo
            elif comando == 'F':
                self.criarProcessoFilho(processo)
            #Substituir o programa (TRoca de contexto)
            elif comando == 'R':
                pass
            #Caso não entre em nenhum dos comandos acima!
            else:
                print("Comando Inexistente!\n")
            processo.adicionarInstrucao(nome)
            #if self.CPU.passarQuantum():
                #pass #FICARIA O MUDAR O PROCESO