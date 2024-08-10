letra = input('Digite uma letra: ').lower()[0]

match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print('Vogal')
    case _:
        print('Consoante')
