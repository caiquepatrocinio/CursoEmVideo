frase= str(input('Digite uma frase : ')).upper().strip()
print('Esta frase possui {} letras A'.format(frase.count('A')))
print('A primera letra A da frase esta na posição : {}'.format(frase.find('A')+1))
print('A ultima letra A da frase esta na posição : {}'.format(frase.rfind('A')+1))