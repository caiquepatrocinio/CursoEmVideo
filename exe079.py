val = list()
while True:
    n = int (input('Digite um numero: '))
    if n not in val:
        val.append(n)
        print('numero adicionadoo')
    else:
        print('Numero duplicado, não sera adicionado.')
    resp = 'SN'
    resp = str(input('Deseja Continuar ? {S/N} ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str (input('Deseja Continuar ? {S/N} ')).strip().upper()[0]
    val.sort()
    if resp == 'N':
        break
print('*'*30)
print(val)
print('Fim do programa')
