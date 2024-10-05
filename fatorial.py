def fatorial(n):
    if n < 0:
        raise ValueError("O número deve ser não-negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = 5
print(f"O fatorial de {numero} é {fatorial(numero)}.")
