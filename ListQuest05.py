numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

if (numero_1 > numero_2 and numero_1 > numero_3):
    print(f'{numero_1} é o maior número')

elif(numero_2 > numero_1 and numero_2 > numero_3):
    print(f'{numero_2} é o maior número')

elif(numero_3 > numero_1 and numero_3 > numero_2):
    print(f'{numero_3} é o maior número')

else:
    print('Todos os números são iguais')
