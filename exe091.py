from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
ranking = []
print('#'*30)
print('      Jogos Sorteados ')
print('#'*30)
for k, v in jogo.items():
    print(f'O jogador {k} jogou {v}.')
    sleep(1)
print('#'*30)
print('   ==Ranking dos Jogadores==')
ranking = sorted(jogo.items() , key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar , foi {v[0]} com {v[1]} pontos..')
    sleep(1)
