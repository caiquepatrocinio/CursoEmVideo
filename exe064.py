n = c = soma = 0
while n != 999:
    n = int (input('Digite um numero: '))
    if n != 999:
        c += 1
        soma += n
print ('Até parar o programa , foram digitados {} numeros e a soma total desses numeros  é de {}'.format(c, soma))