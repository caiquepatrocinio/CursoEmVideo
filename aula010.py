n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2) / 2
if m>= 7 :
    print('Aluno aprovado')
else :
    print('Aluno reporvado')
print('A nota foi {:.1f}'.format(m))
print("*"*20)