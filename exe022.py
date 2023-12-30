
nome = str(input('Digite seu nome : ')).strip()
print('Seu nome em letras maiusculas ', nome.upper())
print('Seu nome em letras minusculas ',nome.lower())
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome é {}, e possui {} letras !'.format((nome[0]),len(nome[0])))
