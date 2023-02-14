from datetime import date, datetime
trabalhador = dict()
print(date.today())
trabalhador['nome'] = input('Digite o nome do trabalhador: ')
nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['carteira de trabalho'] = int(input('Digite a carteira de trabalho: '))
if trabalhador['carteira de trabalho'] != 0:
        trabalhador['ano de contratação'] = int(input('Digite o ano de contratação: '))
        trabalhador['salario'] = float(input('Digite o salário do trabalhador: '))
        trabalhador['aposentadoria'] = (trabalhador['ano de contratação'] + 35)
print(trabalhador)
