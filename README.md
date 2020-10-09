# Ambiente Virtual
### Preparar o ambiente
Comando para instalar o gerenciador de pacotes: `sudo apt install python3-pip`

Comando para instalar o ambiente virtual: `pip3 install virtualenv`

### Ativar o ambiente virtual
Na pasta do projeto, basta executar: `. venv/bin/activate`

### Realizar a instação de alguma lib
Com o módulo ativado, basta executar: `venv/bin/pip3 install nome-do-modulo`

### Módulos já instalados
Para visualizar tudo que está instalado no ambiente, basta executar o comando: `venv/bin/pip3 freeze`

Para gravar a saída do comando acima em um arquivo, basta executar: `venv/bin/pip3 freeze > requirements.txt`

Para instalar todos os módulos do venv caso seja necessário uma confuguração inicial novamente, basta executar o comando: `venv/bin/pip3 install -r requirements.txt`

# Git Flow
A utilização do git-flow visa melhorar o desenvolvimento. 

### Nova feature
Quando você for iniciar uma nova feature. Execute o comando: `git flow feature start MYFEATURE`

Esse comando irá criar uma branch só sua, assim, nada do que você fizer irá interferir no código do outro, e nem quebrará o projeto. A recíproca é verdadeira.

### Integrar feature
Quando você finalizar a tarefa, basta executar o comando: `git flow feature finish MYFEATURE`

Esse comando irá destruir a sua branch e irá integrar o que você produziu na branch principal (develop)

Para mais detalhes bastar acessar o link do [cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html)

# Guia de Estilo para o Python

* **Pacote e nomes de módulos**
    * Os módulos devem ter nomes pequenos, sendo estes escritos em minúsculo por completo. Ex: package

* **Nomes de classes**
    * Os nomes de classes têm a primeira letra de cada palavra maiúscula (CamelCase). Ex: NomeDeUmaClasse

* **Nomes de funções e métodos**
    * Nomes de funções e métodos devem estar em letras minúsculas, com palavras separadas por underscores conforme seja útil para a legibilidade. Ex: nome_de_uma_funcao

* **Constantes**
    * Constantes são geralmente definidas em um nível de módulo e escritas em letras maiúsculas com underscores separando as palavras. Exemplos incluem MAX_OVERFLOW e TOTAL.

* **Nomes de variáveis e parâmetros de funções e métodos**
    * Geralmente seguem a mesma regra das funções, devendo estar em letras minúsculas, com palavras separadas por underscores conforme seja útil para a legibilidade.

    * Obs: Usar self como primeiro parâmetro de um método. Ex: nome_de_um_metodo(self):

* **Identação**
    * A identação deve ser feita usando quatro espaços por nível.
