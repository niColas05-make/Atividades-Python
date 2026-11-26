code=int(input("Digite o código: "))
if(code==1234):
    print("Usuário válido")
    senha=int(input("Digite a senha: "))
    if(senha==9999):
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuário inválido")        