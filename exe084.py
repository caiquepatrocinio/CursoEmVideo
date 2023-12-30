pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str (input('Nome: ')).upper())
    dados.append(int (input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = "SN"
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == "N":
        break
print('x'*40)
print('FIm do programa')
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas. ')
print (f'O menor peso cadastrado foi de {menor} kg, e foram:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print(f'\nO maior peso cadastrado foi: {maior} kg, e foram: ',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')