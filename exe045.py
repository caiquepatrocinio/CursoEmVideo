import random
print('Jogo Pedra/Papel/Tesoura')
print('Coloque 0 para escolher PEDRA')
print('Coloque 1 para escolher PAPEL')
print('Coloque 2 para escolher TESOURA')
op = int (input('QUAL ELEMENTO VOCÊ VAI ESCOLHER? '))
lista = [ 0, 1, 2]
sort = random.choice(lista)
print('o sistema ecolheu ',sort)
if sort == op:
    print('JOGO EMPATADO')
elif sort == 0 and op == 1:
    print('VOcê Ganhou de mim pois eu escolhi PEDRA e você PAPEL ! ')
elif sort == 1 and op == 0:
    print('Ganhei , pois eu escolhi PAPEL e você PEDRA')
elif sort == 0 and op == 2:
    print('Ganhei , pois eu escolhi PEDRA e você TESOURA.')
elif sort == 2 and op == 0:
    print('Você VENCEU , pois eu escolhi TESOURA e você PEDRA')
elif sort == 1 and op == 2:
    print('Você VENCEU , pois eu escolhi PAPPEL e você TESOURA')
elif sort == 2 and op == 1:
    print('Ganhei , pois eu escolhi TESOURA e você PAPEL.')

