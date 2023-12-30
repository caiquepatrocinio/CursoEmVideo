import random
from time import sleep
cont = 0
sort = 0
num = 1
while sort != num :
    print('*'*10,'JOGO DE ADVINHAÇÃO','*'*10)
    num = int(input('Digite um nuemro de 1 até 10 : '))
    lista = [1,2,3,4,5,6,7,8,9,10]
    sort = random.choice(lista)
    print("PROCESSANDO...")
    sleep(2)
    print('O numero sorteado pelao sistema foi {}'.format(sort))
    if sort == num:
        print('Parabéns , você acertou o numero')
    else:
        print('Ganhei de você , tente outra vez')
        cont +=1
print('Você precisou de {} tentativas para me vencer '.format(cont))
print('*'*10,'AGREDECEMOS PELA PREFERÊNCIA','*'*10)