import moeda

p = float (input('Qual éo preço R$? '))
print(f' O preço é {moeda.moeda(p)}, e com desconto ficara  {moeda.moeda(moeda.metada(p))}')
print(f' O preço é {p}, e o seu dobro é  {moeda.moeda(moeda.dobrar(p))}.')
t = float (input('Qual é a taxa que você deseja? '))
print('<= '*15)
print(f'O valor {moeda.moeda(p)} com acrecimos de {t:.2f}% ficara {moeda.moeda(moeda.aumentar(p,t))}.')
print(f'o valor do seu produto é de R$ {moeda.moeda(p)}, e com desconto ficara por R${moeda.moeda(moeda.diminuir(p,t))}.')