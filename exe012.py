val=float(input('Qual o valor do produto?R$  '))
p=float(input('porcentagem de desconto: '))
novo = val - (val*p/100)
#d=val*0.05

print('Este produto que custava R${},com o desconto de {}% esta saindo por R${:.2f}'.format(val, p, novo))