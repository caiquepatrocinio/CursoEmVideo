print('ALISTAMENTO OBRIGATÓRIO PARA HOMENS')
idade = int (input('Digite sua idade: '))
if idade < 18:
    al = 18 - idade
    print('Ainda faltam {} ano(s) para você se alistar , volte com 18 anos completos !! !'.format(al))
elif idade == 18:
    print('Você ja pode se alistar , procure o quanto antes uma base do Exército!')
elif idade > 18 :
    al = idade - 18
    print('Você deveria ter se alistado a {} ano(s), procure o quanto antes uma base militar para se alistar  !!'.format(al))