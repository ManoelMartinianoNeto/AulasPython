def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"


def calculadora():
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif operacao == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif operacao == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Operação inválida")

calculadora()




