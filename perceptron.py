class Perceptron_Class():

    #Inicialização dos valores
    pesos = (0.75, 0.5, -0.6)
    vies = 1
    aprendizagem = 0.2
    diferenca_Class_Result = 0
    registro_validados =[]
    concluir_treinamento = False


    #Inicia o treinamento do perceptron
    def treinamento(self,registros_base):
        print('\n> Início do Treinamento ->')
        print('Σ = x1*peso1 + x2*peso2 + vies*peso3')
        while self.concluir_treinamento is False:
            self.treinamento_perceptron(registros_base)
        
        # #Realiza chamada para predição passando os valores fixados
        # self.predicao_perceptron([2,2])
    
    
    #Treinamento do perceptron - chama as funções de cálculo e faz a vericações
    def treinamento_perceptron(self,registros_base):
        
        #Para facilitar as verificações, ajundando a realizar os cálculos para cada registro
        for item in range(len(registros_base)):
            self.registro_validados.append(True)
        
        #Para facilitar as verificações, ajundando a realizar os cálculos para cada registro
        while len(self.registro_validados) > 0:
            for registro in registros_base:
                registro_classificado = False
                while registro_classificado is False:
                    resultado = self.somatorio(registro[:])
                    classificacao = registro[2]
                    if self.ativacao_f(resultado,classificacao) is True:
                        self.registro_validados.pop(0)
                        registro_classificado = True
                    else:
                        self.diferenca_Classificacao_Resultado(resultado,classificacao)
                        self.calculo_pesos(registro[:])
                        self.registro_validados.clear()
                        return "Recalcular registros"
        print('\nConclução do treinamento. Pesos Finais: ',self.pesos)
        self.concluir_treinamento = True

    
    #Realiza o somatório dos registro, (cálculo da função)
    def somatorio(self,registros):
        resultado = 0
        index = 0
        registros = self.inserir_vies(registros)
        
        #Realiza o somatório
        for registro in registros:
            resultado += registro * self.pesos[index]
            index+=1
        
        #Verifica a função de ativação
        if resultado >= 0:
            ativacao_f = 1
        else:
            ativacao_f = -1
        
        print("\nPesos atuais: " + str(self.pesos) + " -> Registro atuais: " 
            + str(registros) + " -> Somatório: (" + str(resultado) + ")" + 
            " -> Resultado da função: ( " + str(ativacao_f) + " )")
        return ativacao_f

    
    #Realiza o cálculo dos novos pesos
    def calculo_pesos(self,registros):
        resultado = self.diferenca_Class_Result * self.aprendizagem
        registros = self.inserir_vies(registros)
        resultado_todos_registros = [valor * resultado for valor in registros]
        novos_pesos =[]
        for index in range(len(resultado_todos_registros)):
            novos_pesos.append(round(self.pesos[index] + resultado_todos_registros[index],4) )
        self.pesos = novos_pesos
    
    
    #Insere o viés
    def inserir_vies(self,registros):
        #Se o registro for de treinamento, substui a classificação pelo viés para realizar o perceptron.
        #Senão, insere o viés no registro de predição para realizar o preceptron.
        if len(registros) > 2 :
            registros.pop(2)
        registros.append(self.vies)
        return registros
    
    
    #Função de Ativação
    def ativacao_f(self,resultado,classificacao):
        if resultado == classificacao:
            return True
        return False
    
    
    #Parte do recalculo dos pesos - Faz a subtração da Classificação menos o Resultado
    def diferenca_Classificacao_Resultado(self,resultado,classificacao):
        self.diferenca_Class_Result = classificacao - resultado

    
    #Realiza a predição
    def predicao_perceptron(self,registro_predicao):
        print('\n\n> Predição')
        resultado = self.somatorio(registro_predicao[:])
        print('\nClassificacao da predição',registro_predicao," -> Resultado: ",resultado)


if __name__ == '__main__':

    #Instância do Perceptron
    perceptron_ = Perceptron_Class()

    #Base de treinamento para o perceptron
    base_de_treinamento = [
          [1, 1, 1]
        , [9.4, 6.4, -1]
        , [2.5, 2.1, 1]
        , [8, 7.7, -1]
        , [0.5, 2.2, 1]
        , [7.9, 8.4, -1]
        , [7, 7, -1]
        , [2.8, 0.8, 1]
        , [1.2, 3, 1]
        , [7.8, 6.1, -1]
    ]
    
    #Chamada do treinamento
    perceptron_.treinamento(base_de_treinamento)

    print('\n\nPara realizar a predição, insira os valores')
    x1 = input('\nInsira o 1º valor do registro para a predição: ')
    x2 = input('Insira o 2º valor do registro para a predição: ')
    
    print('\n[x1,x2] => [' + x1 + ',' + x2 + ']')
    
    #Realiza a chamada passandos os valores de entrada para realizar a predição
    perceptron_.predicao_perceptron([int(x1),int(x2)])