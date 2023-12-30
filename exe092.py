func = {}
while True:
    func ['nome'] = str (input('Nome: ')).upper()
    func['idade'] = int(input('Idade: '))
    func ['ctps'] = int (input('Numero da carteira de trabalho: '))
    if func['ctps'] == 0:
        break
    func ['contratação'] = int (input('Ano de contratação: '))
    func ['Saláio'] = float (input('valor do salário: '))
    if func['Saláio'] > 0:
        break
print('<=>'*10)
for k, v in func.items():
    print(f' *  {k} esta com o valor {v}')

