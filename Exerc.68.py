from random import randint
cont = 0
while True:
    computador = randint(1,10)
    jogador = int(input('Digite um número: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I]').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if jogador+computador % 2 == 0:
            print('Você Venceu')
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if jogador+computador % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'O número de vitórias consecutivas do jogador é de {cont}')
