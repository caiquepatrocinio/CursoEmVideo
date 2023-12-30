print('lojão das variedades ')
vlprod = float (input('Qual o valor do produto R$: '))
print('Informe a fomar de pagamento:')
print('Digite 1 para pagamento a vista ')
print('Digite 2 para Cartão de Crédito a vista ')
print('Digite 3 para parcelar em até 2 vezes ')
print('Digite 4 para parcelar em 3 vezes ou mais.')
op = int (input('Digite a opção de pagamento desejada: '))
if op == 1:
    vlprod = vlprod - (vlprod * 0.10)
    print('Suas compras deram R$ {:.2f}, você ganhou 10% de desconto'.format(vlprod))
elif op == 2:
    vlprod = vlprod - (vlprod * 0.05)
    print('Suas compras deram R$ {:.2f}, você ganhou 10% de desconto'.format(vlprod))
elif op == 3:
    print('Suas compras deram R$ {:.2f}, que serão parcelasem 2 vezes !!'.format(vlprod))
elif op == 4:
    vlprod = vlprod + (vlprod * 0.20)
    print('Suas compras deram R$ {:.2f}, que serão parcelas em 3 vezes ou mais '.format(vlprod))
else
    print('OPÇÃO INVALIDA ')
