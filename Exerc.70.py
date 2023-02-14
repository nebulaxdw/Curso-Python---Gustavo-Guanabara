total_gasto_compra = 0
quantidade_produtos_acima_1000 = 0
nome_produto_mais_barato = []
cont = 0
while True:
    nome = input('Digite um nome: ')
    preço = float(input('Digite o preço do produto: '))
    cont += 1
    resp = input('Deseja continuar cadastrando mais pessoas? [Ss|Nn]')
    produto_mais_barato = preço
    total_gasto_compra += preço
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    if preço > 1000:
        quantidade_produtos_acima_1000 += 1
    if resp in  'Ss':
        continue
    else:
        break

print(f'O total gasto na compra é de {total_gasto_compra}')
print(f'O número de produtos que custam mais de R$1000,00 é {quantidade_produtos_acima_1000}')
print(f'O produto mais barato custa R${menor:.2f}')
