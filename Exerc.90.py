aluno = {}
while True:
    aluno['nome'] = input('Digite o nome do aluno: ')
    aluno['média'] = float(input('Digite a média do aluno: '))
    if aluno['média'] >= 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'
    resp = input('Quer continuar cadastrando alunos? [Ss][Nn]')
    if resp in 'Nn':
        break
    
for i, x in aluno.items():
    print(f'{i} é igual a {x}')


        
