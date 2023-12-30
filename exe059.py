n1 = n2 = r1 = op= 0
while op != 5:
    n1 = int (input('Digite um numero: '))
    n2 = int (input('Digite outro numero: '))
    print ('[1] SOMAR')
    print ('{2} MULTIPLICAR')
    print ('[3] MAIOR')
    print ('[4] NOVOS NUMEROS')
    print ('[5] sair')
    op = int (input('>>>>>>Digite a opção desejada<<<<<<< '))
    if op == 1:
        r1 = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, r1))
    elif op == 2:
        r1 = n1 * n2
        print('A multiplicação entre {} X {} é {}.'.format(n1, n2, r1))
    elif op == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O maior numero entre {} e {} é {}'.format(n1, n2, n2))
    elif op == 4:
        print('Escolha novos numeros e uma nova opção')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        op = int(input('Digite a opção desejada '))

print('======FIM DO PROGRAMA , AGRADECEMOS A PREFERÊNCIA=======')