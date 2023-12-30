nome = str (input('Qual é o seu nome ? '))
if nome == 'Caique':
    print('Que nome lindo')
elif nome =='Pedro' or nome=='Tiago' or 'Joao':
    print('Este nome é popular no Brasil!')
else:
    print('Este nome é normal')
print('tenha um bom dia, {}!'.format(nome))