def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobrar(preco):
    res =  preco * 2
    return res


def metada(preco):
    res = preco / 2
    return res