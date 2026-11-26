lst = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
lista = []
i=1
soma =0  
for o in list:
    baude = int(input(f"indique a temperatura do mes: {i}\n "))
    lista.append (baude)
    i = i+1
i = 0
for o in lista:
    soma = soma + lista[i]
    i = i+1
media = soma/12
i =0
print (f"a media anual da temperatura foi de: {media}\n")
for x in lst:
    if(lista[i]>media):
        print(f"{lst[i]} é maior que a media com a temperatura de:{lista[i]}")
    else:
        print (f"{lst[i]} é menor que a media com a temperatura de:{lista[i]}")     
    i = i +1    

   