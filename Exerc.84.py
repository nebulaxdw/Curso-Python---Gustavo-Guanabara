lista = []
princ = []
maior = menor = 0
while True:
    lista.append(input('Digite um nome: '))
    lista.append(float(input('Digite um peso: ')))
    if len(princ) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    princ.append(lista[:])
    lista.clear()
    resp = input('Deseja continuar adicionando pessoas? [S|s][N|n]')
    if resp in 'Nn':
        break

print(f'O número de pessoas que foram cadastradas é de {len(princ)} pessoas. Peso de ', end='')
print(f'\nO maior peso foi de {maior}Kg.')
for i in princ:
    if i[1] == maior:
        print(f'{i[0]}', end='')
print()
print(f'\nO menor peso foi {menor} Kg.')

for i in princ:
    if i[1] == menor:
        print(f'{i[0]}', end='')
print()
