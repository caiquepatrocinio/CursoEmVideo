num = list()
pares = list()
impares = list()
mult3 = list()
while True:
    num.append(int (input('Digite um numero: ')))
    resp = 'SN'
    resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str (input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('<=>'*40)
print(f'Lista completa: {num}.')
print(f'lista de numeor PARES : {pares}.')
print(f'Lista de numeros IMPARES: {impares}.')
