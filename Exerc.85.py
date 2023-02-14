#Minha Solução
lista = []
pares = []
impares = []
cont = 1
while cont <= 7:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    cont += 1

lista.append(pares[:])
lista.append(impares[:])
print(sorted(lista))


#Solução do Professor Guanabara

núm = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor%2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
num.sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
