from datetime import date
atual= date.today().year
maior = 0
menor = 0
for c in range (1,8):
    ano = int(input('Digite o ano de nascimento da {}º psssoa : '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print('São {} pessoas maiores de idade '.format(maior))
print('São {} pessoas menores de idade '.format(menor))