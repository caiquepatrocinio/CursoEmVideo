def aumentar(preco= 0, taxa = 0):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco= 0, taxa = 0):
    res = preco - (preco * taxa / 100)
    return res


def dobrar(preco=0):
    res =  preco * 2
    return res


def metada(preco=0):
    res = preco / 2
    return res


def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.'',')