print('-'*10,'PRIMEIRO E ULTIMO NOMES','-'*10)
n = str (input('DIGITE UM NOME : ')).strip().upper()
nome = n.split()
print('Muito prazer !!')
print('O primeiro nome é {}'.format(nome[0]))
print('o ultimo nome é {}'.format(nome[len(nome)-1]))


