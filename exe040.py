print('CALCULO DE MÉDIAS')
n1 = float (input('PRIMEIRA NOTA DO ALUNO : '))
n2 = float (input('SEGUNDA NOTA DO ALUNO : '))
m = (n1 + n2) / 2
if m < 5:
    print('A média foi {}, aluno foi Reprovado !!'.format(m))
elif m == 5 or m < 6.99:
    print('A media foi {}, aluno esta de Recuperação!'.format(m))
elif m >= 7 :
    print('A média foi {}, aluno foi Aprovado!'.format(m))