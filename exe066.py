c = s = m = menor = maior = 0
print('>>>>>Inicio do Programa<<<<<')
while True :
    n = int (input('Digite um numero: '))
    if n == 999:
        break
    c += 1
    s += n
    m = s / c
    if n == 0:
        n = menor
        n = maior
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'Ao todo você inseriu {c} numeros , a soma foi de {s}, tendo uma média de {m:.2f}')
print(f'O menor numero digitado foi {menor} e o maior numero foi {maior}')
print('>>>>>Fim do programa<<<<<')