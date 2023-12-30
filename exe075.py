num = (int (input('Digite um numero: ')),
       int (input('Digite outro numero: ')),
       int (input('Digite mais um numero: ')),
       int (input('Digite o ultimo  numero: ')))
print (f'Você digitou os seguintes numeros {num}.')
print(f'O numero 4 apareceu {num.count(4)} vezes')
if 3 in num:
    print (f'O numero 3 apareceu pela primeira vez na posição {num.index(3)}')
else:
    print('Não foi digitado nenhum valor 3.')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 ==0 :
        print(n, end=' ')
