from random import randint
from time import sleep


def sorteio (lista):
    print('Sorteando 5 numeros em uma lista.', end=' ')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)


def spar (lista):
    print('\nNA soma dos numero PARES da lista temos :',end=' ')
    soma = 0
    for c in lista :
        if c % 2 == 0:
            soma += c
    print(soma)

numeros = []
sorteio(numeros)
spar(numeros)