# Ambiente Virtual
## Preparar o ambiente
Comando para instalar o gerenciador de pacotes: `sudo apt install python3-pip`

Comando para instalar o ambiente virtual: `pip3 install virtualenv`

## Ativar o ambiente virtual
Na pasta do projeto, basta executar: `. venv/bin/activate`

## Realizar a instação de alguma lib
Com o módulo ativado, basta executar: `venv/bin/pip3 install nome-do-modulo`

## Módulos já instalados
Para visualizar tudo que está instalado no ambiente, basta executar o comando: `venv/bin/pip3 freeze`

Para gravar a saída do comando acima em um arquivo, basta executar: `venv/bin/pip3 freeze > requirements.txt`

Para instalar todos os módulos do venv caso seja necessário uma confuguração inicial novamente, basta executar o comando: `venv/bin/pip3 install -r requirements.txt`

# Git Flow
A utilização do git-flow visa melhorar o desenvolvimento. 

Quando você for iniciar uma nova feature. Execute o comando: `git flow feature start MYFEATURE`

Esse comando irá criar uma branch só sua, assim, nada do que você fizer irá interferir no código do outro, e nem quebrará o projeto. A recíproca é verdadeira.

Quando você finalizar a tarefa, basta executar o comando: `git flow feature finish MYFEATURE`

Esse comando irá destruir a sua branch e irá integrar o que você produziu na branch principal (develop)

Para mais detalhes bastar acessar o link do [cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html)