media = []
dados = []
m = n1 = n2 = 0

while True:
    dados.append(str (input('nome: ')).strip().upper())
    n1 = float (input('Nota 1: '))
    n2 = float (input('Nota 2: '))
    m = (n1 + n2) / 2
    dados.append(n1)
    dados.append(n2)
    dados.append(m)
    media.append(dados[:])
    dados.clear()
    resp = 'SN'
    resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str (input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('*'*40 )
print(f'{"nº":<4}{"Nome":<10}{"Média":>8}')
print('*'*40, )
for i , m in enumerate(media):
    print(f'{i:<4}{m[0]:<10}{m[3]:>8} ')
print('*'*40)
while True:
    naluno = int (input('Qual aluno você deseja saber a nota ?(999 interrompe programa) '))
    print('*' * 40)
    if naluno == 999:
        print('Finalizando...')
        break
    if naluno <= len(media) - 1:
        print(f'As notas do aluno {media[naluno][0]}, são {media[naluno][1]} e {media[naluno][2]} ')
print('*'*40)
print('FIM DO ProGRAMA')
