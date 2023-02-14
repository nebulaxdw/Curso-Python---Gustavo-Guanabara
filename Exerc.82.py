lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar adicionanando números na lista? [S|s][N|n]')
    if resp in 'Nn':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(lista)
print(pares)
print(impares)
            
