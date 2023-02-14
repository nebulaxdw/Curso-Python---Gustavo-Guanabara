ficha_aluno = list()
while True:
    nome = input('Digite o nome de um aluno: ')
    nota_1 = float(input('Digite a nota 1 do aluno: '))
    nota_2 = float(input('Digite a nota 2 do aluno: '))
    media = (nota_1 + nota_2) / 2
    if nome not in ficha_aluno:
       ficha_aluno.append([nome])
    else:
        print('Os dados do aluno não serão cadastrados pois eles já foram cadastrados.')
        continue
    ficha_aluno.append([nota_1,nota_2])
    ficha_aluno.append([media])
    resp = input('Deseja continuar cadastrando mais alunos? [S|s][N|n]')
    if resp in 'Nn':
        break

print(ficha_aluno[2])
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha_aluno):
    print(f'{a[1]:<5}{a[0]:<30}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha_aluno) - 1:
        print(f'Notas de {ficha_aluno[opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE >>>')
