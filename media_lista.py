def media_lista(numeros):
    if not numeros:
        return 0  
    return sum(numeros) / len(numeros)

lista_exemplo = [10, 20, 30, 40]
resultado = media_lista(lista_exemplo)
print(f"A média da lista é: {resultado}.")
