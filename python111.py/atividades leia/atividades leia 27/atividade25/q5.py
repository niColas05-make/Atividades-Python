def vogais(palavra):
    contador= 0
    vogais= "aeiouAEIOU"
    for letra in palavra:
        if letra in vogais:
            contador+=1
    return contador
p=input("Digite a sua palavra: ")
print("O numero de vogais na palavra é: ",vogais(p))
