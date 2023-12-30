nome = input('Qual o nome do Funcionario ? ')
sal = float (input('Valor do salário atual ? '))
nsal=sal*0.15+sal
ta=sal*0.15
print('o novo salario do(a) {}, sera de R${:.2f}, aumento salaria de R${:.2f}, Parabéns!!'.format(nome, nsal, ta))