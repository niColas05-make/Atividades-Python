numero1 = int(input("digite o primeriro numero: "))
numero2 = int(input("digite o segundo numero: "))
operacao = input("digite a operacao: ")

match operacao:
    case "+":
        res = numero1 + numero2
    case "-":
        res = numero1 - numero2   
    case "*":
        res = numero1 * numero2
    case "/":
        res = numero1 / numero2

print ("resultado é igual a { res }")                 