h1=int(input("Digite a idade do primeiro homem: "))
h2=int(input("Digite a idade do segundo homem: "))
m1=int(input("Digite a idade da primeira mulher: "))
m2=int(input("Digite a idade da segunda mulher: "))
homem_velho=max(h1, h2)
homem_novo=min(h1, h2)
mulher_velha=max(m1, m2)
mulher_nova=min(m1, m2)
soma= homem_velho + mulher_nova
produto= homem_novo * mulher_velha
print("soma da idades", soma)
print("produto da idades", produto)