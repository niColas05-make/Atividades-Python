list=[ ]
i =0
soma=0
for x in range (1,8):
  temp = int(input("adicione as 7 temperaturas desejadas: "))
  list.append(temp)
  print("lista final: ",list)

for x in range(1,8):
 temp_min=min(list)
 temp_max=max(list)
 soma = soma + list[i]
 i  =i+1
media = soma/7
i = 0
print("\nvalor min da lista",temp_min,"\nvalor max da list", temp_max)
print(f"a media das temperaturas é igual a: {media}")




  



