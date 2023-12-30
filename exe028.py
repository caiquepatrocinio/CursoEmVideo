import random
from time import sleep
print('*'*10,'JOGO DE ADVINHAÇÃO','*'*10)
num = int(input('Digite um nuemro de 1 até 6 : '))
lista = [1,2,3,4,5,6]
sort = random.choice(lista)
print("PROCESSANDO...")
sleep(3)
print('O numero sorteado pelao sistema foi {}'.format(sort))
if sort == num:
    print('Parabéns , você acertou o numero')
else:
    print('Você errou , tente outra vez')
print('*'*10,'AGREDECEMOS PELA PREFERÊNCIA','*'*10)