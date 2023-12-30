somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('-----{}º Pessoa----- '.format(c))
    nome = str (input('Nome: ')).strip()
    idade = int (input('Idade: '))
    sexo = str (input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
            totmulher20 = totmulher20 + 1

mediaidade = somaidade / 4
print('A média de idade das pessoas é de {} anos'.format(mediaidade))
print('O nome do homem mais velho é {}, e sua idade é de {} anos '.format(nomevelho, maioridadehomem))
print('São {} mulheres com idade inferior a 20 anos '.format(totmulher20))