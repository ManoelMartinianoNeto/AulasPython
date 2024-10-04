def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero"
    return num1 / num2

def calcular(num1, num2, operacao):
    operacoes = {
        'somar': somar,
        'subtrair': subtrair,
        'multiplicar': multiplicar,
        'dividir': dividir
    }
    
    if operacao in operacoes:
        return operacoes[operacao](num1, num2)
    else:
        return "Operação inválida"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (somar, subtrair, multiplicar, dividir): ")

resultado = calcular(num1, num2, operacao)
print("Resultado:", resultado)
