a = int(input("adicione 1 numero: "))
b = int(input("adicione 1 numero: "))
c = int(input("adicione 1 numero: "))

def maior(a,b,c):
   
    for x in range(1,4):
        if(a >b and a >c):
            return f"{a}"
        elif(b>c and b>a):
            return f"{b}"
        else:
            return f"{c}"
print(maior(a,b,c))        
            

    
