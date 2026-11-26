cidade=["Maracanau", "Canide", "Boa viagem, fortaleza, caucaia"]
cidade = input("qual cidade vc gostaria de procurar?: ").upper().strip()

if cidade not in (cidade):
    print(f"Cidade não encontrada ")
else:
    print(f"A cidade {cidade} foi encontrada: {cidade.index(cidade)}")
 

