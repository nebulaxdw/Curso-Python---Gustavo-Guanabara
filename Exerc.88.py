lista = []
jogos = list()
from random import randint
quant = int(input('Digite o número de jogos da MEGA SENA que serão gerados: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
      num = randint(1,60)
      if num not in lista:
        lista.append(num)
        cont += 1
      if cont >= 6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os números sorteados foram {jogos}')

for i, l in enumerate(jogos):
    print(f'{i}°Jogo: {l}')

#MINHA SOLUÇÃO

x= []
if quant == 1:
    x.append(randint(1,60))

else:
    for i in range(6):
        x.append([randint(1,60)])
    for i in range*
    
print(x)
