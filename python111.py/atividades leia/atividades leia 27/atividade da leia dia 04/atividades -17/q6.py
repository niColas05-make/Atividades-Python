num = []
nump = []

for x in range(1, 11):
    m = int(input("Adicione 10 números inteiros: "))
   
    num.append(m)
for x in num:
    if x % 2 == 0:
        nump.append(x)

# Percorre e mostra os números da lista nump
for x in nump:
    print("Número par:", x)