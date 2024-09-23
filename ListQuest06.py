print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')
turno = input('Que turno você estuda? ').lower()

match turno:
    case 'm':
        print('Bom dia!')
    case 'v':
        print('Boa tarde!')
    case 'n':
        print('Boa noite!')
    case _:
        print('Valor inválido!')
