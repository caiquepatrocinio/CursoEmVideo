num = [[],[]]
valor = 0
for c in range (0,7):
    valor = int (input(f'Digite o {c+1}º numero: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
    num[0].sort()
    num[1].sort()
print('*'*40)
print(f'OS numeros PARES digitados foram: {num[0]}.')
print(f'Os numeros IMPARES digitados foram : {num[1]}.')



