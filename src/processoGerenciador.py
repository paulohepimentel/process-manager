import os
#from copy import deepcopy
from cpu import CPU
from processoImpressao import ProcessoImpressao
from processoSimulado import ProcessoSimulado
from tabelaProcessos import TabelaProcessos
from variavelProcesso import VariavelProcesso
from memoria import Memoria

class ProcessoGerenciador:

    def __init__(self):
        print('\n\t\t\t🔵🔵🔵 Iniciando o Processo Gerenciador! 🔵🔵🔵\n')
        self.idProcesso = 0
        self.tempo = 0
        self.tempoCPU = 0
        self.estadoExec = 0
        self.CPU = CPU()
        self.estadoPronto = []
        self.estadoBloqueado = []
        self.tabelaProcesso = TabelaProcessos()
        
        self.memoriaPrimaria = Memoria()
        self.memoriaSecundaria = Memoria()

        # Definição da opção de escalonamento
        print('Como você gostaria que os processos fossem escalonados?')
        print('➡️  H - Escalonar por prioridade mais alta')
        print('➡️  X - Escalonar por número de instruções')
        while(True):
            self.modoDeEscalonamento = input('📌  Escolha uma opção: ').upper()
            if self.modoDeEscalonamento == 'H' or self.modoDeEscalonamento == 'X':
                break
            else:
                print('❌ Erro! Entrada inválida\n')
        print('\n')

        # Definição da opção de impressão
        print('Como você gostaria de imprimir o estado do sistema?')
        print('➡️  D - Impressão detalhada')
        print('➡️  S - Impressão simplificada')
        while(True):
            self.modoDeImpressao = input('📌  Escolha uma opção: ').upper()
            if self.modoDeImpressao == 'D' or self.modoDeImpressao == 'S':
                break
            else:
                print('❌ Erro! Entrada inválida\n')
        print('\n')

        self.criarProcessoSimulado(
            eProcessoInicial = True
        )
        print('🔵Gerenciador🔵 criou um 🟡Simulado🟡')


    # * Método relacionado aos comandos recebidos do processo controle através do pipe
    def recebeComandoDoControle(self, comandoRecebido):
        # Comando U: Fim de uma unidade de tempo. O tempo passa quando o U é recebido.
        if(comandoRecebido == 'U'):
            self.executarProcessoSimulado()
            self.tempo+=1
            print('\n⏰ O tempo foi incrementado. Tempo Atual: ' + str(self.tempo))
            print('\n'+('-'*90)+'\n')

        # Comando L: Desbloqueia o primeiro processo simulado na fila bloqueada.
        elif(comandoRecebido == 'L'): 
            self.processoBloqueadoParaPronto()
            print('🔵Gerenciador🔵 desbloqueou o primeiro processo da fila de bloqueados\n')

        # Comando I: Imprime o estado atual do sistema.
        elif(comandoRecebido == 'I'):
            print('🔵Gerenciador🔵 irá criar o 🟢Impressão🟢\n')

            # Pipe -> r para leitura e w para escrita
            rpipe, wpipe = os.pipe()
            idProcesso = os.fork()

            # Processo pai: Processo Gerenciador
            if idProcesso != 0:
                os.write(wpipe, self.modoDeImpressao.encode())
                os.wait() # Espera pelo processo filho

            # Processo filho: Processo Impressão
            if idProcesso == 0:
                self.modoDeImpressao = os.read(rpipe, 32)
                self.modoDeImpressao = self.modoDeImpressao.decode()

                '''
                    - número médio de fragmentos externos;
                    - tempo médio de alocação em termos de número médio de nós percorridos na alocação;
                    - o percentual de vezes que uma requisição de alocação é negada. Neste caso o processo
                    ficaria bloqueado com uma flag de espera por memória. Quando houvesse a liberação de
                    memória por um processo, a alocação deste processo poderia ser tentada novamente.
                '''

                processoImpressao = ProcessoImpressao()

                if(self.modoDeImpressao == 'D'):
                    processoImpressao.impressaoDetalhada(self.tabelaProcesso)
                elif(self.modoDeImpressao == 'S'):
                    processoImpressao.impressaoSimplificada(self.tabelaProcesso)
                print('\n\t\t\t🟢🟢🟢 Finalizando o Processo Impressão! 🟢🟢🟢\n')
                exit()

        # Comando M: Imprime o tempo médio do ciclo e finaliza o sistema.
        elif(comandoRecebido == 'M'):
            # tempo médio = (soma do tempo de cpu de todos os processos não finalizados) / (todos os processos)
            tempoMedio = float(self.tempoCPU/self.idProcesso)
            print('⏰ Tempo de CPU: %.4f' % (self.tempoCPU))
            print('⏰ Numero total de processos: %d' % (self.idProcesso))
            print('⏰ Tempo Médio do Ciclo: %.4f' % (tempoMedio))
            print('\n👋 Encerrando Sistema!')
            print('\n\t\t\t🔵🔵🔵 Finalizando o Processo Gerenciador! 🔵🔵🔵\n')
            exit()


    # * Funções do Processo Gerenciador:
    # * Função 1: Criar um novo processo simulado
    def criarProcessoSimulado(self, eProcessoInicial, contadorAtual=0):
        if eProcessoInicial:
            self.processoSimulado = ProcessoSimulado(
                idProcesso = self.idProcesso, 
                contadorPrograma = 0,
                tempoInicio = 0
            )
            arquivo = open('init.txt', 'r') # Processo simulado inicial
            for instrucao in arquivo:
                self.processoSimulado.adicionarInstrucao(instrucao.replace("\n",""))
            arquivo.close()
            self.tabelaProcesso.adicionarProcesso(self.processoSimulado)
            self.inserirNaListaDeProntos(self.processoSimulado)

        else:
            processoSimulado = ProcessoSimulado(
                idProcesso = self.idProcesso, 
                contadorPrograma = contadorAtual,
                tempoInicio = self.tempo, 
                idPai = self.processoSimulado.idProcesso, 
                estado = 1, # Pronto
                prioridade = self.processoSimulado.prioridade
            )
            processoSimulado.variaveis = self.processoSimulado.variaveis.copy()
            processoSimulado.instrucoes = self.processoSimulado.instrucoes.copy()
            self.tabelaProcesso.adicionarProcesso(processoSimulado)
            self.inserirNaListaDeProntos(processoSimulado)

        self.idProcesso += 1

    # * Função 2: Substituir a imagem atual de um processo simualdo por uma nova imagem
    def substituirImagemProcessoAtual(self, arquivo, processoSimulado):
        processoSimulado.contadorPrograma = 0
        processoSimulado.instrucoes = []
        processoSimulado.variaveis = {}
        
        with open(arquivo) as file:
            for line in file:
                processoSimulado.adicionarInstrucao(line.replace("\n",""))

    # * Função 3: Gerenciar a transição de estados do processo
    def inserirNaListaDeProntos(self, processoSimulado):
        processoSimulado.estado = 1
        if processoSimulado.idProcesso in self.estadoPronto:
            self.estadoPronto.append(processoSimulado.idProcesso)

    def processoBloqueadoParaPronto(self):
        if len(self.estadoBloqueado) > 0:
            idProcesso = self.estadoBloqueado.pop(0)
            self.estadoPronto.append(idProcesso)
            self.tabelaProcesso.atualizarEstadoProcessoPorIndice(
                idProcesso = idProcesso,
                estado = 1 # Pronto
            )

    def processoProntoParaBloqueado(self, processoSimulado):
        if len(self.estadoPronto) > 0:
            self.estadoBloqueado.insert(self.estadoPronto.pop(0))
            processoSimulado.estado = 0

    # * Função 4: Escalonar os processos
    def escalonadorDeProcessos(self):
        if(self.modoDeEscalonamento == 'H'):
            self.estadoPronto = self.tabelaProcesso.ordenarProcessosProntos()
        elif(self.modoDeEscalonamento == 'X'):
            self.estadoPronto = self.tabelaProcesso.ordenarNumeroInstrucoes()

        if self.estadoPronto == []:
            self.processoSimulado = None
        else:
            print('✴️  Proximo processo: %d' % self.estadoPronto[0])
            self.processoSimulado = self.tabelaProcesso.buscarProcesso(self.estadoPronto[0])
            self.CPU.quantumUsado = 0
            self.trocaDeContexto(self.processoSimulado)

    # * Função 5: Realizar a troca de contexto
    def trocaDeContexto(self, processoSimulado):
        self.tabelaProcesso.defineProcessoEmExecucao(processoSimulado)

    # * Método relacionado a execução do processo simulado
    def executarProcessoSimulado(self):
        if self.processoSimulado == None and len(self.estadoPronto) > 0:
            self.escalonadorDeProcessos()
        
        if self.processoSimulado != None:
            self.CPU.executarProcesso(self.processoSimulado)
            self.processoSimulado = self.CPU.processoEmExecucao
            print('\n🟡 Executando o processo de ID: ' + str(self.processoSimulado.idProcesso))
            if self.processoSimulado.instrucoes != []:
                self.processoSimulado.estado = 2 # Em execução
                print('📑 Instruções do processo atual: ', end='')
                for i in self.processoSimulado.instrucoes:
                    print (i, end='; ')
                #print ('\n')
                instrucao = self.processoSimulado.instrucoes.pop(0)
                instrucaoDividida = instrucao.split()
                comando = instrucaoDividida[0]

                # ​1. Comando N: número de variáveis que serão declaradas neste processo simulado
                if comando == 'N':
                    numDeVariveis = int(instrucaoDividida[1])
                    variaveisDoProcesso = []
                    for i in range(numDeVariveis):
                        variavel = VariavelProcesso(self.processoSimulado.idProcesso)
                        variaveisDoProcesso.append(variavel)

                    memoriaTemEspaco = self.memoriaPrimaria.algoritmoWorstFit(variaveisDoProcesso)
                    if(not memoriaTemEspaco):
                        '''
                            Processo é bloqueado e entra para a memória secundária com a flag de 
                            requisição de espaço (flag pode ser abstraída, já que se o processo foi 
                            bloqueado ele está aguardando a memória primária).
                        '''
                        pass

                # 2. Comando D: Declara uma variável inteira X, valor inicial igual a 0
                elif comando == 'D':
                    '''
                    self.processoSimulado.declaraVariavel(
                        indice = int(instrucaoDividida[1])
                    )
                    for v in variaveisDoProcesso:
                        if v.nome == None:
                            v.nome =
                    '''


                # 3. Comando V: Define o valor da variável inteira x
                elif comando == 'V':
                    self.processoSimulado.defineValor(
                        indice = int(instrucaoDividida[1]), 
                        valor = int(instrucaoDividida[2])
                    )

                # 4. Comando A: Adiciona n ao valor da variável inteira x
                elif comando == 'A':
                    self.processoSimulado.somaValor(
                        indice = int(instrucaoDividida[1]),
                        valor = int(instrucaoDividida[2])
                    )

                # 5. Comando S: Subtrai n do valor da variável inteira x
                elif comando == 'S':
                    self.processoSimulado.somaValor(
                        indice = int(instrucaoDividida[1]),
                        valor = -int(instrucaoDividida[2])
                    )

                # 6. Comando B: Bloqueia esse processo simulado
                elif comando == 'B':
                    self.processoSimulado.estado = 0 # Bloqueado
                    self.estadoBloqueado.append(self.processoSimulado.idProcesso)
                    self.estadoPronto.remove(self.processoSimulado.idProcesso)

                # 7. Comando T: Termina o processo simulado
                elif comando == 'T':
                    self.estadoPronto.remove(self.processoSimulado.idProcesso)
                    self.tabelaProcesso.removerProcesso(self.processoSimulado)
                    self.processoSimulado = None

                # 8. Comando F: Cria um novo processo simulado filho
                elif comando == 'F':
                    self.criarProcessoSimulado(
                        eProcessoInicial = False,
                        contadorAtual = int(instrucaoDividida[1]),
                    )

                # 9.​ Comando R: Substitui o programa do processo pelo programa no arquivo
                elif comando == 'R':
                    self.substituirImagemProcessoAtual(str(instrucaoDividida[1]), self.processoSimulado)

            self.tempoCPU += 1
            if comando != 'T':
                self.processoSimulado.tempoCPU += 1
                self.tabelaProcesso.atualizarProcesso(self.processoSimulado)

                if self.processoSimulado.instrucoes == []:
                    # As instruções do processo foram concluídas, remover o processo
                    self.estadoPronto.remove(self.processoSimulado.idProcesso)
                    self.tabelaProcesso.removerProcesso(self.processoSimulado)
                    self.processoSimulado = None

                if self.CPU.passarQuantum() and self.processoSimulado.instrucoes != []:
                    # Processo gastou o quantum disponível
                    self.processoSimulado.incrementarPrioridade()
                    self.tabelaProcesso.atualizarProcesso(self.processoSimulado)
                    self.escalonadorDeProcessos()

                if comando == 'B':
                    self.tabelaProcesso.atualizarProcesso(self.processoSimulado)
                    self.escalonadorDeProcessos()