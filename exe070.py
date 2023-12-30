soma = tot1000 = menor = cont = 0
barato = ''
print ('=' *30)
print('++ SUPERMERCADO BAHIAS MAR ++')
while True:
    print('=' * 30)
    nome = str (input('Nome do Produto: ')).strip().upper()
    valor = float (input('Valor do produto R$: '))
    cont += 1
    soma += valor
    if valor < 1000:
        tot1000 += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str (input('Deseja continuar suas compras? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print ('=' *30)
print ('Agradecemos pela sua preferência !!!')
print(f'O total da sua compra é de R${soma:.2f}.')
print(f'Temos {tot1000} produtos custando abaixo de R$ 1000,00.')
print(f'o produto mais barato custou R${menor:.2f} e foi o(a){barato}.')