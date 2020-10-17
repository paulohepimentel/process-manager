import os
import time
from processoGerenciador import ProcessoGerenciador

class ProcessoControle:
    
    def __init__(self):
        print('Iniciando o processo controle e esse, cria processo gerenciador!\n')
        self.criaProcessoControle()

    def criaProcessoGerenciador(self, rpipe):
        print('💧 Processo Gerenciador:', os.getpid(), '\n')
        processoGerenciador = ProcessoGerenciador()
        fobj = os.fdopen(rpipe, 'r')
        comando_recebido = os.read(rpipe, 32)
        print('💧 O processo gerenciador leu do pipe o comando: ' + comando_recebido.decode())
        processoGerenciador.recebeComandoDoControle(comando_recebido)

    def criaProcessoControle(self):
        # Pipe -> file descriptors r para leitura e w para escrita
        rpipe, wpipe = os.pipe()
        idProcesso = os.fork()

        if idProcesso > 0:
            # Processo pai: Processo Controle
            comando = ''
            os.close(rpipe)
            print('🔥 Processo Controle:', os.getpid(), idProcesso)
            while(comando != 'M'):
                comando = input().encode()
                #w = os.fdopen(w, 'w')
                os.write(wpipe, comando)
                print('🔥 Comando escrito no pipe para o processo gerenciador: ' + comando.decode())
                #os.close(w)
                time.sleep(1)

        elif idProcesso == 0:
            # Processo filho: Processo Gerenciador
            os.close(wpipe)
            self.criaProcessoGerenciador(rpipe)

processo = ProcessoControle()