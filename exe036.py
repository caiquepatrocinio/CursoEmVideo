vlimovel= float (input('uual o valor do imóvel ? '))
sal = float (input('Qual o valor do salario ? '))
ano = int (input('Em quanto anos você deseja pagar ? '))
mes = ano * 12
parc = vlimovel / mes
if parc > (sal * 0.30):
    print('Sua renda não suporta um financiamento deste valor')
elif parc < (sal * 0.30):
    print('Sua parcela sera de R$ {:.2f} mensais, sem juros! '.format(parc))
