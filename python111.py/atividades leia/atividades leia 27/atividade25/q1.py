nome = input("Adicione um nome: ")
periodo = int(input("Adicione o periodo: "))
#adiciona os valores dentro da função
def sauda(nn , hora):
    periodo = hora
    nn = nome

#possibilidades de respostas    
    if(periodo>12 and periodo<18):
        return "boa tarde",nome
    elif(periodo<12 and periodo>5):
        return  "bom dia", nome
    else:
        return "boa noite", nome
    
#saida de informações
print(sauda(nome ,periodo ))
