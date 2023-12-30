num = cont = media = soma  = 0
op = 's'
menor = maior = 0
while op != 'n':
    num = float (input('Digite um numero: '))
    op = str (input('Deseja continuar [S/N]: '.strip()))
    cont += 1
    soma += num
    media = soma / cont
    if num > 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num > menor:
        menor = num
print('=====FIM DO PROGRAMA=====')
print('A media dos numero é de {}'.format(media))
print('O maior numero foi {}.'.format(maior))
print('O menor numero foi {}.'.format(maior))
