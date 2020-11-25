from variavelProcesso import VariavelProcesso
from copy import deepcopy

FREE = 0
class Memoria:
    def __init__(self, tamanho):
        self.numFrag = 0
        self.tamanho = tamanho
        self.memoria = [FREE for i in range(tamanho)]

    def imprimeMemoria(self):
        contador = 0
        print('|', end='')
        for i in self.memoria:
            if contador >= self.tamanho:
                break
            if i == FREE:
                print(' '+ str(i) + ' |', end='')
            else:
                print(' '+ str(i.idProcesso) + '-' + str(i.nome) + '-' + str(i.valor) + ' |', end='')
            contador+=1
        print('\n')
    
    def imprimeTodaMemoria(self):
        print('|', end='')
        for i in self.memoria:
            if i == FREE:
                print(' '+ str(i) + ' |', end='')
            else:
                print(' '+ str(i.idProcesso) + '-' + str(i.nome) + '-' + str(i.valor) + ' |', end='')
        print('\n')

    def imprimeMemoriaVirtual(self):
        contador = 0
        print('|', end='')
        for i in self.memoria:
            if i == FREE and contador>=self.tamanho:
                print(' '+ str(i) + ' |', end='')
            elif(contador>=self.tamanho):
                print(' '+ str(i.idProcesso) + '-' + str(i.nome) + '-' + str(i.valor) + ' |', end='')
            contador+=1
        print('\n')

    def retornaTamanhoMemoria(self):
        return len(self.memoria)
    # Método só confere se existe a possibilidade de inserção
    def retornaEspacoLivreDaMemoria(self):
        tamanho = 0
        index = 0
        maiorEspaco = -1
        for i in self.memoria:
            if i == FREE:
                print(i)
                tamanho+=1
            else:
                # MEXER NISSO, INSERINDO DIRETO NA SECUNDÁRIA
                if (tamanho > maiorEspaco):
                    ('Maior fatia: ' + str(tamanho))
                    maiorEspaco = tamanho
                    index = self.memoria.index(i) - tamanho
                tamanho = 0
        if (tamanho > maiorEspaco):
            ('Maior fatia: ' + str(tamanho))
            maiorEspaco = tamanho
            index = len(self.memoria) - tamanho
        # Maior espaço recebe o tamanho total da memória
    

        print('Espaço: ' + str(maiorEspaco))
        return maiorEspaco, index

    def verificarFragExterna(self,tamanho : int,indiceFinal: int):
        numFrag = 0
        contador = 0
        tamIdentico = 0
        for i in self.memoria:
            if contador >= indiceFinal:
                return numFrag
            if i == FREE:
                tamIdentico+=1
                if tamIdentico == tamanho:
                    tamIdentico = 0
                    numFrag+=1
            else:
                tamIdentico = 0
            contador+=1
        self.numFrag+=numFrag
        return numFrag


    def liberaEspacoDaMemoria(self, idProcesso):
        for index, i in enumerate(self.memoria):
            if i != FREE:
                if i.idProcesso == idProcesso:
                    self.memoria[index] = FREE
        return

    # Método que escolhe a maior porção de memória livre
    def algoritmoWorstFit(self, variavelProcesso):
        memoriaLivre, index = self.retornaEspacoLivreDaMemoria()
        print("Indice: "+str(index))
        print('Espaço livre: ' + str(memoriaLivre))
        if memoriaLivre >= len(variavelProcesso):
            print('Cabe')

            for i in variavelProcesso:
                self.memoria[index] = i
                index +=1
            return True # A alocação foi realizada
        return False # A alocação foi não pôde ser realizada

    # Método que busca variaveis, se o vetor estiver vazio busca na memória secundária
    def buscarVariavelDoProcesso(self, idProcesso):
        variaveis = []
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == idProcesso:
                    variaveis.append(i)
        return variaveis

    def buscaVariavelIndice(self, idProcesso, indice):
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == idProcesso and i.nome == indice:
                    return i
        return False
    
    def preencherVariavel(self, idProcesso, nome, valor):
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == idProcesso and i.nome == None:
                    i.valor = valor
                    i.nome = nome
                    return i
        return False

    def mudarValor(self, idProcesso, nome, valor):
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == idProcesso and i.nome == nome:
                    i.valor = valor
                    return i
        return False

    def desalocarMemoria(self, var:VariavelProcesso):
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == var.idProcesso and i.nome == var.nome:
                    self.memoria[self.memoria.index(i)] = FREE

    def removerProcesso(self, idProcesso):
        variaveis = []
        for i in self.memoria:
            if i != FREE:
                if i.idProcesso == idProcesso:
                    variaveis.append(deepcopy(i))
        for i in variaveis:
            self.desalocarMemoria(i)
        return variaveis

    def inserirSecundaria(self, var:VariavelProcesso):
        self.memoria.append(var)

    def inserirSecundariaVect(self, var):
        for i in var:
            self.memoria.append(i)

    def primeiroProcessoSec(self):
        for i in self.memoria:
            if i != FREE:
                return i.idProcesso


'''
memoria = Memoria(5)
print(memoria.memoria)
v1 = VariavelProcesso(1, 1, 1)
v2 = VariavelProcesso(2, 2, 2)
memoria.algoritmoWorstFit([v1,v2,v1])
memoria.algoritmoWorstFit([v1])
memoria.algoritmoWorstFit([v1])
memoria.algoritmoWorstFit([v1,v2,v1,v2])
memoria.inserirSecundaria(v2)
print(memoria.removerProcesso(2))

#memoria.liberaEspacoDaMemoria(1)
#print()
memoria.imprimeMemoria()
memoria.imprimeMemoriaVirtual()
memoria.imprimeTodaMemoria()
'''