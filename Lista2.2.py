continuar = "s"

while continuar.lower() == "s":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
    
    continuar = input("Deseja fazer outra soma? (s/n): ")

    