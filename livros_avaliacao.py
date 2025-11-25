
def verificaAvaliacao(livros):
        
    while True:

        try:

            pergunta = float(input(f'Avaliação do livro "{livros}" (0 - 10): '))

            if pergunta >= 0 and pergunta <= 10:

                return pergunta
            
            else:
                print('Atenção as orientações apenas números de 0 a 10!')

        except ValueError:
            print('Atenção as orientações, apenas números de 0 a 10!')


def verificaLeitura(livros):
        
    while True:

        leitura = input(f'Situação da leitura do livro "{livros}" ("lendo", "lido","na fila")').upper()
        
        if leitura == 'LENDO' or leitura == 'LIDO' or leitura == 'NA FILA':

            return leitura
        
        else:

            print('Atenção as orientações use apenas: "lendo", "lido","na fila"')


with open ("livros.txt", "r") as livros:
    obra = livros.read()
    conteudo = obra.split("\n")

    listaLivros = []
    y = True

    for dados in conteudo:

        primal = dados.split(",")
        listaLivros.append(primal)

    while y:

        for dados in listaLivros:
            try: 
                avaliacao =  verificaAvaliacao(dados[1])

                leitura = verificaLeitura(dados[1])

            except Exception :
                print('')

            with open ("livros_avaliacao.txt","a") as avaliacaoSalve:
                avaliacaoSalve.write(f'{dados[0]},{dados[1]},{dados[2]},{avaliacao:.2f},{leitura}\n')

        y = False          