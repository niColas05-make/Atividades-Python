cvd= []
for x in range(1, 4):
    nomes = input("Digite os nomes: ")
    cvd.append(nomes)
    print(cvd)

nome = input ("ecolha um nome para remover: ")
cvd.remove(nome)    
print("a lista final ficou: ",cvd)