from random import randint
from time import sleep
contap =  1
lista = []
jogos = []
print('-'*30)
print('     JOGOS NA MEGA SENA     ')
print('-'*30)
ap = int (input('Quantas apostas você deseja fazer: '))
while contap <= ap:
    cont = 0
    while True:
        num = randint (1,25)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contap += 1
print('='*3, f'Sorteando {ap} Jogos', '*'*3)
for i, c in enumerate(jogos):
    print(f'Jogo {i+1} : {c}')
    sleep(1.5)
print('='*30)
print('FIM DO PROGRAMA')