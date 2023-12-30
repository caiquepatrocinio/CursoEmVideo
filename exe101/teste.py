import moeda

p = float (input('Qual éo preço R$? '))
print(f' O preço é R${p:.2f}, e com desconto ficara R$ {moeda.metada(p):.2f}')
print(f' O preço é R${p:.2f}, e o seu dobro é R$ {moeda.dobrar(p):.2f}.')
t = float (input('Qual é a taxa que você deseja? '))
print('<= '*15)
print(f'O valor R${p:.2f} com acrecimos de {t}% ficara R${moeda.aumentar(p,t):.2f}.')
print(f'o valor do seu produto é de R$ {p:.2f}, e com desconto ficara por R${moeda.diminuir(p,t):.2f}.')