val = list()
c = c5 = 0
while True:
    val.append (int (input('Digite um numero: ')))
    resp = 'SN'
    resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    val.sort(reverse=True)
    while resp not in 'SN':
        resp = str (input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('<='*50)
print(f'VOcê adicionou {len(val)} valores')
print(f'Lista em ordem decrescente:  {val}')
if 5 in val:
    print('O numero 5, aparece nos elementos digitados')
else:
    print('O numero 5,não aparece nos elementos digitaoos')
print(f'FIM DO ProGRAMA')
print('<='*50)