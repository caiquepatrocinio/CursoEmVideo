sal = float (input('Qual o salario deste funcionário ? '))
nsal = float
if sal <= 1200:
    nsal = sal * 0.15 + sal
else:
    nsal = sal * 0.10 + sal
print('O funcionario que recebe R$ {:.2f}, passara a receber R$ {:.2f}.'.format(sal , nsal))

