from random import randint
v = 0
print('<->' * 20)
while True:
    jogador = int (input('Digite um numero: '))
    comp = randint(0,11)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str (input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'VOcê jogou {jogador} o sistema Jogou {comp} e a soma deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU !!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU !!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    print('Vamos Jogar novamente ....')
print('*' *20)
print('GAME OVER')
print(f'Você ganhou de mim {v} vezes seguidas !')

