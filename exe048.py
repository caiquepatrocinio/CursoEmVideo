s = 0
for c in range (1,501,2):
    if c % 3 == 0:
        s = s + c
print('A soma do numeros multiplos de 3 até 500 é de {}.'.format(s))