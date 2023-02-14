while True:
    n = int(input('Digite um número: '))
    if n < 0:
     print('O número digitado é negativo e o programa será interrompido')
     break
    print('---------TABUADA-----------')
    for i in range(10):
        print(f'{n} x {i} = {n*i}')
        print('\n')
    print('---------------------------')
   
    
