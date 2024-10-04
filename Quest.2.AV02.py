def contar_digitos(numero):
    return len(str(abs(numero)))

num = int(input("Digite um número inteiro: "))
resultado = contar_digitos(num)
print(f"O número {num} tem {resultado} dígito(s).")


