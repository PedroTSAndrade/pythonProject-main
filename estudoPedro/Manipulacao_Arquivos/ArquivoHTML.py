with open("pagina.html", "w") as pagina:
    pagina.write("<body> <div style=\"text-align:center\"> <h1> Esta é um teste para página WEB </h1>")
    pagina.write("<br><h2> Página Para Teste Adicionando Nomes:  </h2> </div>")
    pagina.write("<h3> Lista de nomes:")
    nome=""
    while nome!="SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome!="SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")