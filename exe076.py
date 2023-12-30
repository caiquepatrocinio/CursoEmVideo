listagem = ('Lapis', 1.50,
            'Borracha', 2.50,
            'Caderno', 15.90,
            'Estoja', 25.00,
            'Tranferidor', 4.25,
            'Compasso',9.90,
            'mochila',125,
            'Canetas', 22.50,
            'Livros',34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')