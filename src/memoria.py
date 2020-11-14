from variavelProcesso import VariavelProcesso

class Memoria:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.memoria = [0 for i in range(tamanho)]

    def retornaTamanhoMemoria(self):
        return len(self.memoria)

    # Método só confere se existe a possibilidade de inserção
    def retornaEspacoLivreDaMemoria(self):
        tamanho = 0
        index = 0
        maiorEspaco = -1
        for i in self.memoria:
            if i == 0:
                tamanho+=1
            else:
                if (tamanho > maiorEspaco):
                    maiorEspaco = tamanho
                    index = self.memoria.index(i) - tamanho
                tamanho = 0

        # Maior espaço recebe o tamanho total da memória
        if maiorEspaco == -1:
            maiorEspaco = len(self.memoria)

        return maiorEspaco, index

    def liberaEspacoDaMemoria(self, idProcesso):
        for index, i in enumerate(self.memoria):
            if i != 0: # Significa que a memória não está vazia
                if i.idProcesso == idProcesso:
                    self.memoria[index] = 0 # Memória vazia
        return

    # Método que escolhe a maior porção de memória que pode
    def algoritmoWorstFit(self, variavelProcesso):
        memoriaLivre, index = self.retornaEspacoLivreDaMemoria()
        if memoriaLivre >= len(variavelProcesso):
            for i in variavelProcesso:
                self.memoria[index] = i
                index +=1
            return True
        return False

    # Método que busca variaveis, se o vetor estiver vazio busca na secundária
    def buscarVariavelDoProcesso(self, idProcesso):
        variaveis = []
        for i in self.memoria:
            if i != 0:
                if i.idProcesso == idProcesso:
                    variaveis.append(i)
        return variaveis


'''
memoria = memoria(5)
print(memoria.memoria)
v1 = VariavelProcesso(1, 1, 1)
v2 = VariavelProcesso(1, 2, 2)
memoria.algoritmoWorstFit([v1, v2])

memoria.liberaEspacoDaMemoria(1)
print(memoria.memoria)
'''