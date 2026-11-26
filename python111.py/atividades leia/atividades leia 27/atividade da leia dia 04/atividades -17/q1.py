def festa(dinheiro, compras):
    if dinheiro>=compras:
        return "compra bem sucedida"
    else :
          falta =  compras - dinheiro
          return f"compra não sucedida, falta {falta} reais"
dinheiro = int(input("insira seu valor inicial: "))
compras = int(input("insira o valor final da compra: "))

print(festa(dinheiro,compras))