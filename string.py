def contar_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador

string_exemplo = "Olá, como você está?"
numero_de_vogais = contar_vogais(string_exemplo)
print(f"Número de vogais: {numero_de_vogais}")
