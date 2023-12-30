from datetime import date
print('*'*8,'OE ANO É BISSEXTO OU NÃO ?','*'*8 )
ano = int (input('DIGITE O ANO OU 0 PARA ANALISAR O ANO ATUAL: '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('{}, esse ano é Bissexto.'.format(ano))
else :
    print('{}, esse ano não é Bissexto'.format(ano))
