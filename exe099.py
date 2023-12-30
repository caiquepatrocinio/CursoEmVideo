def maior(*num):
    cont = maior = 0
    print('--'*20)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont +=1
    print(f'\nForam informados {cont} valores.')
    print(f'\nO maior valor passado foi {maior}')


maior(4, 7, 1, 4, 6, 8)
maior(6, 2, 7, 5)
maior(9, 6, 2, 4, 7, 1, 0)
maior(6, 4, 1)
maior()