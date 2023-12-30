def factorial (num, show=False):
    """
    ->Calculo Factorial de um numero
    :param num: numeroa ser calculado
    :param show: OPcional para mostrar ou não a conta
    :return: O valor da factorial de um numero = num
    """
    f = 1
    for c in range (num , 0 , -1):
        if show:
            print(c, end='')
            if c >1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)

#programa principal
n = int (input('Digite um numeor para ser calculado seu factorial: '))
factorial(n, show=True)
#help(factorial)