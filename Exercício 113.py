def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyBoardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n

    def leiaFloat(msg):
        while True:
            try:
                n = float(input(msg))
            except(ValueError,TypeError):
                print('\033[31mERRO: por favor, digite um número real válido.\033[m')
                return 0
            else:
                return n
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um número de ponto flutuante: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

