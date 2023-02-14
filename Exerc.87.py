matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
soma_terceira_coluna = 0
maior = matriz[1][0]
for i in range(3):
    for j in range(3):
     matriz[i][j] = int(input(f'Digite um valor para ocupar a posição {[i]}{[j]} da matriz: '))

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares+= matriz[i][j]
        if matriz[1][j] > maior:
            maior = matriz[1][j]
    soma_terceira_coluna += matriz[i][2] 


for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}', end='')
    print()

print(f'A soma dos valores pares da matriz é {soma_pares}')
print(f'A soma da terceira coluna da matriz é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha da matriz é {maior}')
            
            


            
    
