matriz = [0]*3
for i in range(3):
    matriz[i] = [0]*3
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um número para a posição {[i]}{[j]} da matriz: '))


for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}', end='')
    print()

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um número para a posição {[i]}{[j]} da matriz: '))
    
for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}', end='')
    print()
