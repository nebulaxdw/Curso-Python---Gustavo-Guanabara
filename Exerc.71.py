total = float(input('Informe o valor que será sacado: '))
céd_50 = 0
céd_20 = 0
céd_10 = 0
céd_1 = 0
while total >= 50:
    total = total - 50
    céd_50 += 1
while total >= 20:
    total = total - 20
    céd_20 += 1
while total >= 10:
    total = total - 10
    céd_10 += 1
while total >= 1:
    total = total - 1
    céd_1 += 1

print(f'Serão entregues {céd_50} cédula(s) de R$50,00, {céd_20} cédula(s) de R$20,00, {céd_10} cédula(s) de R$10,00 e {céd_1} cédula(s) de R$1,00 para completar os R${total}')


    
