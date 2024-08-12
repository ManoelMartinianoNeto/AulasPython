# Programa para classificar participação em um crime

# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicializar contador de respostas positivas
respostas_positivas = 0

# Fazer as perguntas e contar as respostas "sim"
for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classificar com base no número de respostas positivas
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibir a classificação
print(f"\nClassificação: {classificacao}")
