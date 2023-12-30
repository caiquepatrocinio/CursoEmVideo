from datetime import date
def voto ():
    nasc = int (input('Qual o ano de nascimento do eleitor? '))
    idade = date.today().year - nasc
    if idade < 16 :
        print(f'Eleitor possui {idade} anos e NÃO ESTA APTO para votar.')
    elif idade >= 16 and idade < 18:
        print(f'Eleitor possui {idade} anos e seu voto é OPCIONAL.')
    elif idade >= 18 and idade < 65:
        print(f'Eleitor possui {idade} anos e seu voto é OBIGATÒRIO.')
    elif idade >= 65:
        print(f'Eleitor possui {idade} anos e seu voto é OPCIONAL.')


voto()
