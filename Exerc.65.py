soma = cont = maior = menor = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    resp = input('Digite [S|s] para continuar digitando números ou [N|n] para parar: ')
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    if(resp in 'Nn'):
        break
    else:
        continue
    
print(f'A média dos números digitados é de {soma/cont}, o maior número é {maior} e o menor é {menor}')
    
