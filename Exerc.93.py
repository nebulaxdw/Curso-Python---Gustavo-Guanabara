dados = dict()
gols = []
dados['jogador'] = input('Digite o nome do jogador: ')
dados['partidas'] = int(input('Digite o número de partidas que ele jogou: '))
dados['total_gols'] = 0
for i in range(dados['partidas']):
 gols.append(int(input(f'Digite o número de gols feitos na {i}° partida: ')))
 dados['gols'] = gols

for i in dados['gols']:
    dados['total_gols'] += i

for i, k in dados.items():
    if i == 'jogador':
        print(f'O jogador é {k}')
    if i == 'partidas':
        print(f'O número de partidas é {k}')

for i, v in enumerate(dados['gols']):
    print(f'Na partida {i}, o jogador fez {v} gols.')

print(f'Foi um total de {dados["total_gols"]}')
