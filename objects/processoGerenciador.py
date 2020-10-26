import os
import time
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
        self.estadoPronto = [] 
        self.estadoBloqueado = [] 
        self.tabelaProcesso = TabelaProcessos()

    def inserirBloqueado(self, processo:ProcessoSimulado):
        self.estadoBloqueado.append(processo.idProcesso)
        processo.mudarEstadoProcesso(0)

    def removerBloqueado(self, processo:ProcessoSimulado):
        self.estadoPronto.insert(self.estadoBloqueado.pop(0))
        processo.mudarEstadoProcesso(1)

    def atualizarEstadosBloqueado(self):
        self.estadoBloqueado = self.tabelaProcesso.ordenarProcessoBloqueados()
    
    def atualizarEstadosBloqueadoNumInstruct(self):
        self.estadoBloqueado = self.tabelaProcesso.ordenarNumeroInstrucoes()

    def inserirPronto(self, processo:ProcessoSimulado):
        self.estadoPronto.append(processo.idProcesso)
        processo.mudarEstadoProcesso(1)

    def inserirProcessoExec(self, processo:ProcessoSimulado):
        self.estadoExec = processo.idProcesso
        processo.mudarEstadoProcesso(2)
    
    def criarProcesso(self):
        novoProcesso = ProcessoSimulado(self.idDosProcessos,0,self.tempo)
        self.inserirProcessoNaTabela(novoProcesso)
        self.inserirBloqueado(novoProcesso)
        self.idDosProcessos+=1
        return novoProcesso

    def criarProcessoFilho(self,processo:ProcessoSimulado, ProgramCounter):
        processoFilho = ProcessoSimulado(self.idDosProcessos,int(ProgramCounter),0,processo.idProcesso,1,processo.prioridade)
        processoFilho.valor = processo.valor.copy()
        self.inserirProcessoNaTabela(processoFilho)
        self.idDosProcessos+= 1

    def substituirImagemProcesso(self,processo:ProcessoSimulado,nomeArquivo:str):
        processo.contadorPrograma = 0
        processo.instrucoes = []
        processo.valor = {}
        with open(nomeArquivo) as file:
            for line in file:
                processo.adicionarInstrucao(line.replace("\n",""))

    def concluirProcesso(self,idProcesso):
        self.estadoPronto.append(idProcesso)
        self.estadoBloqueado.remove(idProcesso)

    def inserirProcessoNaTabela(self, processo:ProcessoSimulado):
        self.tabelaProcesso.adicionarProcesso(processo)

    def removerProcessoNaTabela(self, processo:ProcessoSimulado):
        self.tabelaProcesso.removerProcesso(processo)

    def imprimirListaProcesso(self):
        ProcessoImpressao().impressaoSimplificada(self.tabelaProcesso)

    def imprimirListaProcessoDetalhado(self):
        ProcessoImpressao().impressaoDetalhada(self.tabelaProcesso)

    def calculaTempoMedioCiclo(self):
        soma = 0
        tamTabela = 0
        for processo in self.tabelaProcesso.listaProcessos:
            tamTabela+=1
            if processo.estadoProcesso != 1:
                soma += int(processo.tempoCPU)
        return float(soma/tamTabela)

    def inputComandoDoControle(self):
        while(True):
            print("\n-----------------------------------------------------------")
            print("\t\t\tMENU")
            print("-----------------------------------------------------------")
            print("💻 U, passa uma unidade de tempo")
            print("💻 L, desbloqueia o primeiro processo na fila bloqueada")
            print("💻 I, imprime o estado do sistema")
            print("💻 M, imprime o tempo médio de ciclo e encerra")
            print("-----------------------------------------------------------")
            comandoRecebido = input("💻 Comando Escolhido: ")
            print("-----------------------------------------------------------\n")

            # U: Fim de uma unidade de tempo, enquanto não ocorre o fim, o tempo
            # está parado. O tempo passa quando o comando U é recebido.
            if(comandoRecebido == 'U'):
                self.tempo+=1
                print('⏰ O Gerenciador de Processos incrementou o tempo' + '\n')
                print("⏰ Tempo Atual: "+str(self.tempo))
                return False

            # L: Desbloqueia o primeiro processo simulado na fila bloqueada.
            elif(comandoRecebido == 'L'): 
                print('💧 O gerenciador de processos desbloqueou o primeiro da fila' + '\n')
                return True

            # I: Imprime o estado atual do sistema.
            elif(comandoRecebido == 'I'):
                print('💧 O gerenciador de processos vai criar o processo impressão')
                print("💧 Escolha D para Impressão Detalhada")
                print("💧 Escolha S para Impressão Simplificada")
                tipoImpressao = input("💧 Opção Escolhida: ")
                print("\n")

                # Pipe -> file descriptors r para leitura e w para escrita
                idProcesso = os.fork()
                
                if idProcesso != 0:
                    time.sleep(.1)
                    #thrownAway = input("Digite qualquer tecla para continuar! Este comando será desconsiderado!")

                if idProcesso == 0:
                    if(tipoImpressao == 'D'):
                        print("\t\t\t\t  TABELA DE PROCESSOS")
                        print("---------------------------------------------------------------------------------------------------")
                        print("idProcesso\tidProcessoPai\tEstado\t\tTempo Inicial\tTempoCPU\tValores")
                        print("---------------------------------------------------------------------------------------------------")
                        ProcessoImpressao.impressaoDetalhada(self.tabelaProcesso)
                        print("\n")

                    else:
                        print("          TABELA DE PROCESSOS")
                        print("--------------------------------------------")
                        print("idProcesso\tEstado")
                        print("--------------------------------------------")
                        ProcessoImpressao.impressaoSimplificada(self.tabelaProcesso)
                        print("\n")
                    exit()
                        

            # M: Imprime o tempo médio do ciclo e finaliza o sistema.
            # tempo médio = (soma do tempo de cpu de todos os processos ainda não finalizados) / (todos os processos)
            elif(comandoRecebido == 'M'):
                print('⏰ Tempo Médio do Ciclo: %.4f' % (self.calculaTempoMedioCiclo()))
                print("👋 Encerrando Sistema!")
                exit()
            
            else:
                print('❌ O gerenciador de processos não reconhece o comando: ' + comandoRecebido + '\n')


    
    def inserirInstrucao(self,processo,comando):
        processo.adicionarInstrucao(comando.replace("\n",""))
    

    def simularProcesso(self,processo : ProcessoSimulado):
        #A tabela de processos só é atualziada depois da execução do processo
        processo.mudarEstadoProcesso
        self.CPU.mudarProcesso(processo)

        while self.CPU.processoExecut.instrucoes != []:
            if self.inputComandoDoControle():
                return None

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
                #return NoneD 0
            
            #Soma N do valor da variavel X onde N é um inteiro
            elif comando == 'A':
                self.CPU.processoExecut.somaValor(int(instrucaoDividida[1]),int(instrucaoDividida[2]))
            
            #Cria um processo filho do processo
            elif comando == 'F':
                self.criarProcessoFilho(self.CPU.processoExecut,int(instrucaoDividida[1]))
            
            #Substituir o programa (TRoca de contexto)
            elif comando == 'R':
                self.substituirImagemProcesso(self.CPU.processoExecut,str(instrucaoDividida[1]))
                self.CPU.passarQuantum()
                processo = (self.CPU.processoExecut)
                self.tabelaProcesso.atualizarProcesso(processo)
                return processo

            #Caso não entre em nenhum dos comandos acima!
            else:
                print("Comando Inexistente!\n")

            #self.CPU.processoExecut.imprimeProcessoDetalhado()

            if self.CPU.passarQuantum() and self.CPU.processoExecut.instrucoes != []:
                self.CPU.processoExecut.incrementarPrioridades()
                processo = (self.CPU.processoExecut)
                processo.mudarEstadoProcesso(0)
                self.tabelaProcesso.atualizarProcesso(processo)

                return processo
                #pass #FICARIA O MUDAR O PROCESO
        self.CPU.processoExecut.decrementarPrioridades()
        processo = (self.CPU.processoExecut)
        processo.mudarEstadoProcesso(1)
        self.tabelaProcesso.atualizarProcesso(processo)
        self.concluirProcesso(processo.idProcesso)
        return processo


    def executarAltaPrioridade(self):
        self.atualizarEstadosBloqueado()
        if self.estadoBloqueado == []:
            if self.inputComandoDoControle():
                print("❌ Erro! Não existem mais itens na fila de itens bloqeuados! Você pode imprimir o estado atual ou sair do código!")
            else:
                print("❌ Erro! Não existem mais itens na fila de itens bloqeuados! Você pode imprimir o estado atual ou sair do código!")
        else:
            processoReferente = self.tabelaProcesso.buscarProcesso(self.estadoBloqueado[0])
            print("\n💾 Executando o processo de ID: "+str(self.estadoBloqueado[0]))
            self.simularProcesso(processoReferente)

        self.executarAltaPrioridade()

    def executarMenorNumInstruct(self):
        self.atualizarEstadosBloqueadoNumInstruct()
        if self.estadoBloqueado == []:
            if self.inputComandoDoControle():
                print("Erro! Não existem mais itens na fila de itens bloqeuados! Você pode imprimir o estado atual ou sair do código!")
            else:
                print("Erro! Não existem mais itens na fila de itens bloqeuados! Você pode imprimir o estado atual ou sair do código!")
        else:
            processoReferente = self.tabelaProcesso.buscarProcesso(self.estadoBloqueado[0])
            print("\n💾 Executando o processo de ID: "+str(self.estadoBloqueado[0]))
            self.simularProcesso(processoReferente)

        self.executarAltaPrioridade()

PG = ProcessoGerenciador()
ProcessoA = PG.criarProcesso()
ProcessoB = PG.criarProcesso()
ProcessoC = PG.criarProcesso()
#PG.inserirInstrucao(ProcessoA,"R arquivo.txt")
PG.inserirInstrucao(ProcessoA,"D 0")
PG.inserirInstrucao(ProcessoA,"D 1")
PG.inserirInstrucao(ProcessoA,"V 0 1000")
PG.inserirInstrucao(ProcessoA,"V 1 500")
PG.inserirInstrucao(ProcessoA,"V 0 19")
PG.inserirInstrucao(ProcessoA,"A 0 19")
PG.inserirInstrucao(ProcessoA,"F 1")
PG.inserirInstrucao(ProcessoB,"D 0")
PG.inserirInstrucao(ProcessoB,"D 1")
PG.inserirInstrucao(ProcessoB,"A 0 19")
PG.inserirInstrucao(ProcessoB,"F 1")
PG.executarMenorNumInstruct()