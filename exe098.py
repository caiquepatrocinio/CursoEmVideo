from time import sleep
def contador (a, b):
    for c in range (a,b+1):
        print(f'{c}', end=' ')
def contador1 (a, b):
    for c in range (a,b-1,-2):
        print(f'{c}', end=' ')

def contador2 (a, b, c):
    if a < b:
        b + 2
    elif a > b:
        b - 2
    for cont in range (a,b,c):
        print(f'{cont}', end=' ')
        sleep(1)



print('*'*25)
print('Contagem de 1 até 10 de 1 rm 1.')
contador(1, 10)
print ('FIM')
print()

print('*'*25)
print('Contagem de 10 até 0 de 2 em 2 .')
contador1(10, 0)
print('FIM')
print()

print('*'*25)
a = int (input('Inicio: '))
b = int (input('Final: '))
c = int (input('intervalo: '))
contador2(a, b, c)
print('FIM')
print()

