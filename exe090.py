dados = {}
dados ['Nome'] = str (input('Nome: ')).upper()
dados ['Média'] = float (input(f'Média do aluno(a) {dados['Nome']}: '))
if dados['Média'] < 5:
    dados ['Situação'] = 'Reprovado'
elif dados['Média'] >= 5 and dados['Média'] < 7 :
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Aprovado'
print('-'*40)
for k, v in dados.items():
    print(f' - {k} é igual a {v}.')

