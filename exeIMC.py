peso = float (input('Qual é o seu peso: '))
alt = float (input('Qual é a sua altura : '))
imc = peso / alt ** alt
if imc < 18.5:
    print('\33[1;31mSeu Imc é de {:.2f}, esta abaixo do normal !!\33[m'.format(imc))
if imc >= 18.5 and imc <= 25:
    print('\33[1;34mSeu Imc é de {:.2f}, esta normal !!\33[m'.format(imc))
if imc > 25:
    print('\33[1;31mSeu Imc é de {:.2f}, esta acima do normal !!\33[m'.format(imc))

#print('Sei Imc é de {:.2f}'.format(imc))