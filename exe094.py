lista = []
dados = {}
media = tot = cont = 0
while True:
    dados.clear()
    dados ['Nome'] = str (input('Nome: ')).upper()
    r = 'MF'
    dados ['Sexo'] = str (input('Sexo {M/F}: ')).strip().upper()[0]
    while dados ['Sexo'] not in 'MF':
        dados ['Sexo'] = str(input('Opção Inválida! Sexo: [M/F]: ')).strip().upper()[0]
    dados ['idade'] = int (input('Idade: '))
    lista.append(dados.copy())
    tot += dados['idade']
    cont +=1
    resp = "SN"
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str (input('Opção Inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == "N":
        break
    media = tot / cont
print('='*25)
print(f'      ESTATISTICAS')
print('='*25)
print(f'(A) Foram cadastradas {len(lista)} pessoas.')
print(f'(B) A média de idade das pessoas é de {media:.2f} anos')
print(f'(C) AS mulheres cadastradas foram:.', end=' ')
for p in lista:
   if  p ['Sexo'] in 'Ff':
       print(f'{p['Nome']}', end=' ')
print()
print(f'(D) Lista de pessoas com idade acima da média', end=' ')
print()
for p in lista:
    if p ['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}')
print('='*25)
print('FIM DO PROGRAMA')