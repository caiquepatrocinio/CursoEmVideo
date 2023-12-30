jogador ={}
partida = []
media = 0
jogador ['Nome'] = str (input('Nome: ')).strip().upper()
tot = int (input(f'Quantas partidas {jogador['Nome']} jogou? '))
for c in range (0,tot):
    partida.append(int (input(f'   Quantos gols na partida {c+1}: ')))
jogador ['gols'] = partida[:]
jogador ['total'] = sum(partida)
media = jogador ['total'] / tot
print('=='*20)
print(jogador)
print('=='*20)
for k, v in jogador.items():
    print(f'o campo {k} em o valor {v}.')
print('==' * 20)
print(f'O jagador {jogador['Nome']} fez {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1} forma feitos {v}')
print(f'*** Fez um total de {jogador['total']} gols. ***')
print(f'*** Média de {media:.2f} gols por jogo. ***')
print('==' * 20)
print('FIM DO PROGRAMA')

