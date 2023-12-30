def factorial (n):
    f = 1
    for c in range (n, 0, -1):
        f *= c
    print(f'O factorial de {n} é {f}')

#programa principal
num =int (input('Digite um numero para se calcula o seu factorial: '))
factorial(num)