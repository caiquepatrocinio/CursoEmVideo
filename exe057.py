sexo = str (input('Digete um sexo [M/F] : ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str (input('Dados invalidos , por favor , Digete um sexo [M/F] : ')).strip().upper()[0]
print('Sexo {}, registrado com sucesso '.format(sexo))


