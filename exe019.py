from random import choice
n1 = input('Primeiro Aluno : ')
n2 = input('Segundo Aluno : ')
n3 = input('Terceiro Aluno : ')
n4 = input('Quarto Aluno : ')
l = [n1 , n2, n3, n4]
esc = choice(l)
print('O aluno escolhido foi {}'.format(esc))
