dados = dict()
lista = []
lista_mulheres = []
soma = média = 0
while True:
    dados['nome'] = input('Digite um nome: ')
    dados['sexo'] = input('Digite o sexo da pessoa: [M/F]').upper()[0]
    if dados['sexo'] not in 'MF':  
        print('O sexo digitado não foi o masculino nem o feminino. Tente novamente!')
        continue
    dados['idade'] = int(input('Digite a idade da pessoa: '))
    soma += dados['idade']
    lista.append(dados.copy())
    resp = input('Deseja continuar cadastrando mais pessoas? [S|s][N|n]')
    if resp in 'Nn':
        break
print(lista)

for i, x in enumerate(lista):
    if i == dados['nome']:
        quant_pessoas += 1
média = soma/len(lista)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
    print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

    
    
