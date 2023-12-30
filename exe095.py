jogador ={}
partida = []
time = []
while True:
    jogador.clear()
    partida.clear()
    jogador ['Nome'] = str (input('Nome: ')).strip().upper()
    tot = int (input(f'Quantas partidas {jogador['Nome']} jogou? '))
    for c in range (0,tot):
        partida.append(int (input(f'   Quantos gols na partida {c+1}: ')))
    jogador ['gols'] = partida[:]
    jogador ['total'] = sum(partida)
    resp = "SN"
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    time.append(jogador.copy())
    while resp not in 'SN':
        resp = str (input('Opção Inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == "N":
        break
print('=='*20)
print('COD', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('=='*20)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('=='*20)
while True:
    busca = int (input('Deseja saber dados de qual jogador: (999 interrompe)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO, não existe este código dde busca ')
    else:
        print (f'Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  {i}º partida foram feitos {g} gols. ')
    print('==' * 20)
print('==' * 20)
print('FIM DO PROGRAMA')
print('>>>VOLTE SEMPRE<<<')
