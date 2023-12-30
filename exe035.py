print("<-"*20)
print('ANALISADOR DE TRIANGULOS')
print('<-'*20)
r1 = float (input('Digite o tamanho da linha 1 : '))
r2 = float (input('Digite o tamanho da linha 2 : '))
r3 = float (input('Digite o tamanho da linha 3 : '))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('Os segmentos formam um TRIÂNGULO !!!!!! ')
else:
    print('Os segmentos NÃO formam um TRIÂNGULO !!!')
