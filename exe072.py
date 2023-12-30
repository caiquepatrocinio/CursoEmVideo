cont = ('ZERO','UM','DOIS','TRÊS','QUATRO', 'CINCO','SEIS',
        'SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE',
        'QUATORZE','QUIZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
resp = 'SN'
num = 0
while True:
    print('+++Digite um numero de 0 a 20+++')
    num = int (input('Digite um numero: '))
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    print('='*30)
    if 0 <= num <= 20:
        print(f'Você digitou o numero {cont[num]}')
    else:
        print('Digite um nuemro valido. ')
        num = int(input('Digite um numero: '))
    if resp == 'N':
        break


print('>>>>FIM DO PROGRAMA<<<<')
