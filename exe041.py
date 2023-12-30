idade = int (input('qual é a idade do atleta ? '))
if idade < 9 :
    print('ATLETA MIRIM')
elif idade >=9 and idade < 14:
    print('ATLETA INFANTIL')
elif idade >= 14 and idade < 19:
    print('ATLETA JUNIOR')
elif idade >= 19 and idade < 29:
    print('ATLETA SÊNIOR')
elif idade >= 29:
    print('ATLETA MASTER')