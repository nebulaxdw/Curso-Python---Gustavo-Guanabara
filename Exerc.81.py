lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    resp = input('Deseja continuar adicionando número: [S|s][N|n]')
    if resp in 'Nn':
        break

print(f'A quantidade de números que foram digitados é de {cont}')
print(sorted(lista,reverse=True))

for i in lista:
    if i == 5:
        print('O valor 5 foi digitado e está na lista')
