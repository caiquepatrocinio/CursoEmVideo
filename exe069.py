tot18 = toth = tot20 = 0
while True:
    print('=' * 25)
    idade = int (input('Digite uma idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input('Digite o sexo [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        print('=' * 25)
        resp = str(input('Deseja Continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('>>>>>FIM DO PROGRAMA<<<<<<')
print (f'O total de pessoas maiores de 18 anos é de {tot18}.')
print(f'O total de homens é de {toth}.')
print(f'O total de mulheres com menos de 20 anos é de {tot20}.')

