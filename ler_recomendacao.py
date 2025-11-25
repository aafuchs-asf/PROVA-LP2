with open ("livros_recomendados.txt", "r") as livros:
    print('--------------------------------------')
    print('Top 5 livros: ')
    print(f'{livros.readlines()}')
    print('--------------------------------------')
