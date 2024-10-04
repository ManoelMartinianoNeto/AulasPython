def verificar_numero(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

num = float(input("Digite um número: "))
resultado = verificar_numero(num)
print(f"O resultado é: {resultado}")

