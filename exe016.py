dia = int(input('Quantos dias você ficará com o carro ? '))
km = int(input('Quantos kilometros você rodou ? '))
tot= (dia * 60) + (km * 0.15)
print('*' *45)
print ('Você pagará R$ {}, pelo aluguel do carro !!'.format(tot))
print('*' *45)