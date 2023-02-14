times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético','Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(times[1:5])
print(times[-4:])
print(sorted(times))
for i, x in enumerate(times):
    if x == 'Chapecoense':
        print(f'O time da Chapecoense está na {i}° posição')
print(f'O Chapecoense está na {times.index("Chapecoense")} °posição')
