altura = int(input("adicione a aultura do retangulo: "))
largura = int(input("adicione a largura do retangulo: "))

#adiciona os valores dentro da função
def area(altura,largura):
    calc = largura * altura

#retorna o valor da area
    return 'o valor da area é de', calc
print(area(altura,largura))
