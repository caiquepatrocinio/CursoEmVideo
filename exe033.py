a = int (input('Primeiro Numero : '))
b = int (input('Segundo Numero : '))
c = int (input('Terceiro Numero : '))
#Verificando o menor valor
menor = a
if b<a or b<c:
    menor = b
if c<a or c<b:
    menor = c
#Verificando o maior valor
maior = a
if b>a or b>c:
    maior = b
if c>a or c>b:
    maior = c

print('o maior numeros é {}, e o menor numero é {}'.format(maior, menor))
