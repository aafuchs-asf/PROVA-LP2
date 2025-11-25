with open ("livros_avaliacao.txt", "r") as livros:
    obra = livros.read()
    conteudo = obra.split("\n")

    listaRecomenda = []

    for dados in conteudo:

        primal = dados.split(",")

        if primal[0] != '' and primal[4] != 'NA FILA':

            listaRecomenda.append(primal[3])

        


    listaRecomenda.sort(key = lambda x: (-x[3], x[1]))
    livros5 = listaRecomenda[:5]
    print(f'{livros5} : top 5')
