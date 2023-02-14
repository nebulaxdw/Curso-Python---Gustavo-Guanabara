soma = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        print('O número 999 foi digitado e programa irá parar')
        break
    soma += n
    cont += 1
print(f'A soma de todos os números digitados é de {soma} e a média é de {soma/cont}')

