val = list()
for cont in range (0,5):
    val.append(int(input(f'Digite um numero para a posição {cont} : ')))
print(f'Você digitou os seguintes numeros: {val}')
print(f'O maior valor digitado foi {max(val)} na posição {val.index(max(val))}.')
print(f'O menor valor digitado foi {min(val)} na paosição {val.index(min(val))}.')