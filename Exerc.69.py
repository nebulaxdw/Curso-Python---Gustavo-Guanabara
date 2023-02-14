cont_maior_18= 0
cont_homens = 0
cont_mulheres = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa: [M|m][F|f]')
    resp = input('Deseja continuar cadastrando mais pessoas: [S|s][N|n]')
    if idade > 18:
        cont_maior_18 += 1
    if sexo in 'Mm':
        cont_homens += 1
    if sexo in 'Ff' and idade < 20:
        cont_mulheres += 1
    if resp in 'Ss':
        continue
    else:
        break
print(f'A quantidade de pessoas que tem mais de 18 anos é de {cont_maior_18}')
print(f'A quantidade de homens cadastrados é de {cont_homens}')
print(f'A quantidade de mulheres cadastradas menores de 20 anos é de {cont_mulheres}')

        
