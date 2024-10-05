def converter_temperatura(valor, escala):
    if escala == 'C':
        return (valor * 9/5) + 32
    elif escala == 'F':
        return (valor - 32) * 5/9
    else:
        raise ValueError("Escala inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")

temp_c = 25
temp_f = converter_temperatura(temp_c, 'C')
print(f"{temp_c}°C em Fahrenheit é {temp_f}°F.")

temp_f = 77
temp_c = converter_temperatura(temp_f, 'F')
print(f"{temp_f}°F em Celsius é {temp_c}°C.")
