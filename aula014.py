'''from time import sleep
c = 0
print('PROCESSANDO ....')
while c < 10:
    sleep(2)
    c += 1
    print(c)
print('FIM')
'''

n = 1
par = impar = 0
while n != 0:
    n = int (input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('no total teve {} numeros pares e {} numeros impares'.format(par, impar))
