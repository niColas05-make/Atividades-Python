compras = []
for x in range (1,6):
  itens = input("adicione seus itens: ")
  compras.append(itens)
  print ("list after appending: ",compras)
print ("\nseu primeiro produto foi",{compras[0]}, "e seu segundo foi ", {compras[4]})