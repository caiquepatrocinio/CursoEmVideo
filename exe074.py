from random import randint
num = (randint (1,10),randint (1,10),randint (1,10)
       ,randint (1,10),randint (1,10))
print('Os numeros sorteados foram: ', end='')
for n in num :
       print(n, end='  ')
print(f'\nO maior numero sorteado foi {max(num)}. ')
print(f'O menor numero sorteado foi {min(num)}.')