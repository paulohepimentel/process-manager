<h1 align="center">
    <img alt="Logo" title="Simulator" src="images/logo.png" width="500px" />
</h1>

<p align="center">
  <a href="#-projeto">Projeto</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tipos-de-processos">Tipos de Processos</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-política-de-escalonamento">Política de Escalonamento</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-iniciar-a-simulação">Iniciar a Simulação</a>
</p>

## ✦ Projeto
<p align="justify">
A proposta deste trabalho prático consistiu na implementação de um sistema que 
realiza a simulação de um gerenciador de processos, conceito abordado na disciplina, 
sendo muito utilizado nos sistemas operacionais.
</p>

<p align="justify">
O trabalho desenvolvido funciona como um gerenciador de processos do sistema 
operacional Linux, ou seja, demonstrando seus dados e estruturas através do 
terminal. O fluxo do sistema, começa através do ProcessoControle, que a 
partir dele será criado (fork) o ProcessoGerenciador, que além de gerenciar os processos 
simulados também poderá criar (fork) o ProcessoImpressao.
</p>

## ✦ Tipos de Processos
Para o simulador, a implementação de três processos foi feita. Um quarto também
foi implementado, mas esse basicamente é apenas um processo simulado, esses são
os que serão gerenciados.

**Processo Controle:**
- Realiza um fork, cria um pipe e inicia o Processo Gerenciador
- Recebe comandos do usuário
- Recebe comandos: 
  - U: Passa uma unidade de tempo
  - L: Desbloqueia um processo
  - I: Imprime o estado atual do sistema
  - M: Imprime o tempo de ciclo médio e encerra o sistema

**Processo Gerenciador:**
- Controla a tabela de processos
- Controla o estado dos processos: Prontos, bloqueados, em execução e finalizados
- Realiza o escalonamento de processos com base em prioridades
- Simula operações para os processo simulados, controlando o uso da CPU
- Realiza um fork, cria um pipe e inicia o Processo Impressão

**Processo Impressão:**
- Imprime o estado atual da tabela de processos de duas formas
  - Impressão simples: ID do Processo | Prioridade | Estado do Processo
  - Impressão detalhada: ID do Processo | ID do Processo Pai| Prioridade | Estado do Processo | Tempo Inical | Tempo de CPU | Instruções

**Processo Simulado:**
<p align="justify">
A simulação de gerenciamento de processo gerencia a execução de processos simulados.
Cada processo simulado é composto de um programa que manipula (define/atualiza) o
valor de variáveis inteiras. Dessa forma, o estado de um processo simulado, a qualquer
momento, é composto pelos valores da suas variáveis inteiras e pelo valor do seu
contador de programa.
</p>

## ✦ Politica de Escalonamento
<p align="justify">
A política de escalonamento tem como princípio a ideia de atribuir aos processos, 
determinadas prioridades de acordo com o seu número de execuções. Dessa maneira, 
um processo não ocupa por tempo indeterminado toda a CPU, otimizando assim, o 
sistema completamente.
</p>

<p align="justify">
As prioridades iniciam em zero (prioridade mais alta) e vai até três(prioridade 
mais baixa), ou seja, quatro classes de prioridades. Assim, para cada classe 
atribuída a um processo, esse possuía um tempo para executar as suas instruções, 
ou seja, tempo de CPU.
</p>

## ✦ Iniciar a Simulação
<p align="justify">
Para a execução do programa é necessário instalar a dependência <a href="">PrettyTable</a>. Essa dependência auxilia na visualização dos resultados pelo terminal:
</p>

- Comando para instalação: `pip3 install prettytable`

Para a inicialização do sistema, dentro da pasta src, basta chamar o arquivo processoControle.py
- Comando para iniciar o sistema: `python3 processoControle.py`


---
<p align="justify">
O projeto foi desenvolvido, para fins didáticos, durante a disciplina de Sistemas Operacionais do curso de Bacharelado em Ciência da Computação da UFV – Campus Florestal
</p>
