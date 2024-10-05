def contar_palavras(s):
    palavras = s.split()
    return len(palavras)
    
string_exemplo = "Olá, como você está?"
numero_de_palavras = contar_palavras(string_exemplo)
print(f"Número de palavras: {numero_de_palavras}.")
