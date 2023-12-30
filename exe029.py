print('*'*10,'RADAR DE VELOCIDADE','*'*10)
vel = float(input('Qual a velocidade o carro passou ? '))
vmulta = float
if vel > 80 :
    print('Você foi multado')
    vmulta = (vel - 80) * 7
    print('O valor da multa sera de R$ {:.2f}'.format(vmulta))
print('TENHA UM BOM DIA !!!')

