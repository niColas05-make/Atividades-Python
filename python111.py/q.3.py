morango=float(input("Digite quantos kgs de morango voce quer: "))
maca=float(input("Digite quantos kgs de maca voce quer: "))
kgt= morango + maca
if(morango<=5):
    valormorango= morango * 2.50 
else:
    valormorango= morango * 2.20

    if(maca<=5):
        valormaca= maca * 1.80
    else:
        valormaca= maca * 1.50
        precof= valormorango + valormaca
        if(kgt>8) or (precof>25):
            total = precof * 0.9
        else:
            total = precof
print("O kg total de frutas compras é", kgt, "Voce tera que pagar um valor de", total)

        

