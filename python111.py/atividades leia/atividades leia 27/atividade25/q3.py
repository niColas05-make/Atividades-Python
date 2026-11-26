num = int(input("Digite um numero: "))
def eh_par(num):
    if(num%2==0):
        return "True"
    else:
        return "False"
print(eh_par(num))