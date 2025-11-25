with open ("livros_avaliacao.txt", "r") as livros:
    obra = livros.read()
    conteudo = obra.split("\n")

    listaRecomenda = []

    for dados in conteudo:

        primal = dados.split(",")

        if primal[0] != '' and primal[4] != 'NA FILA':

            listaRecomenda.append(primal)

        
    listaRecomenda.sort(key = lambda avaliacao: float(avaliacao[3]), reverse=True)
  
    livros5 = listaRecomenda[:5]

    with open ("livros_recomendados.txt", "a") as arquivo:
        arquivo.write(f'{livros5}')
