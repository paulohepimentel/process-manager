import os
from processoGerenciador import ProcessoGerenciador
from prettytable import PrettyTable

class ProcessoControle:

    def __init__(self):
        print('\n\t\t\t🔴🔴🔴 Iniciando o Processo Controle! 🔴🔴🔴\n')
        self.numComandos = 0
        self.criaProcessoControleEGerenciador()


    # * Menu explicativo referente aos comandos que podem ser recebidos
    def menu(self):
        '''
        print("Menu de comandos disponíveis:")
        print('➡️  U - Fim de uma unidade de tempo')
        print('➡️  L - Desbloqueia o primeiro processo simulado na fila bloqueada')
        print('➡️  I - Imprime o estado atual do sistema')
        print('➡️  M - Imprime o tempo médio do ciclo e finaliza o sistema')
        print()
        '''

    # * Método responsável pela criação processo controle e realizar o fork para
    # * a criação do processo gerenciador
    def criaProcessoControleEGerenciador(self):
        # Pipe -> r para leitura e w para escrita
        rpipe, wpipe = os.pipe()
        idProcesso = os.fork()

        # Processo pai: Processo Controle
        if idProcesso > 0:
            self.menu()
            print('Como você gostaria de inserir os comandos?')
            print('➡️  A - Entrada manual')
            print('➡️  B - Arquivo de entrada')

            while (True):
                opcaoEntrada = input("📌 Escolha uma opção: ").upper()
                if opcaoEntrada == 'A' or opcaoEntrada == 'B':
                    break
                else:
                    print('❌ Erro! Opção inválida, tente novamente')

            comandos = ''
            if(opcaoEntrada == 'A'):
                comandos = self.recebeComandoManual()
            elif(opcaoEntrada == 'B'):
                comandos = self.recebeComandoArquivo()

            # Escreve os comandos recebidos no pipe para o Processo Gerenciador
            os.write(wpipe, comandos.encode())
            os.wait() # Espera pelo processo filho
            print('\n\t\t\t 🔴🔴🔴 Finalizando o Processo Controle! 🔴🔴🔴\n')
            exit()

        # Processo filho: Processo Gerenciador
        elif idProcesso == 0:
            # Lê do pipe os comandos escritos pelo Processo Controle
            comandosRecebidos = os.read(rpipe, 1000)
            comandosRecebidos = comandosRecebidos.decode()

            processoGerenciador = ProcessoGerenciador()

            i = 0
            for comando in comandosRecebidos:
                i+=1
                print('🔵Gerenciador🔵 irá executar agora o comando nº ' + str(i) +': ' + comando)
                processoGerenciador.recebeComandoDoControle(comando)


    # * Métodos relacionados a entrada de comandos
    def recebeComandoArquivo(self):
        comando = ''
        comandos = ''

        print('\n🤖 Modo entrada manual ativado')
        nomeDoArquivo = input("📄  Entre com o nome arquivo: ")

        arquivo = open(nomeDoArquivo, 'r') # Lietura do arquivo externo
        for comando in arquivo:
            comando = comando.replace('\n','')
            if(comando != 'U' and comando != 'L' and comando != 'I' and comando != 'M'):
                print('❌ Erro! O Arquivo possui um comando inválido, ele será ignorado.')
            else:
                comandos += comando
        arquivo.close()
        print('🔰 Lista de comandos recebidos: ', end='')
        print(*comandos, sep =", ")
        return comandos

    def recebeComandoManual(self):
        comando = ''
        comandos = ''
        print('\n😃 Modo entrada manual ativado')
        while comando != 'M':
            comando = input("📌 Escolha um comando: ").upper()
            if(comando != 'U' and comando != 'L' and comando != 'I' and comando != 'M'):
                print('❌ Erro! Comando inválido, tente novamente')
            else:
                comandos += comando
        print('🔰 Lista de comandos recebidos: ', end='')
        print(*comandos, sep =", ")
        return comandos

# * Inicia o sistema
simuladorDeProcessos = ProcessoControle()