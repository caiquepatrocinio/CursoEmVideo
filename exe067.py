print('>>>>>>>PROGRAMA DAS TBUADAS<<<<<<<')
c = mult = 0
while True:
    print('=============================================')
    mult = int (input('QUal o numero você deseja fazer a tabuada: '))
    print('=============================================')
    if mult < 0:
        break
    for c in range (1,11):
        r = c * mult
        print(f'{mult} x {c} = {r}')
print('>>>>>FIM DO PROGRAMA<<<<<')
