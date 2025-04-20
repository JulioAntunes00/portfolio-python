# Programa para converter temperatura de Celsius para Fahrenheit

# Solicita a temperatura em graus Celsius
temp = float(input("Digite a temperarua em ºC: "))

# Aplica a fórmula de conversão para Fahrenheit
fahrenheit = (temp * 9/5)+32

# Exibe o resultado com duas casas decimais
print(f"{temp:.2f}°C é igual a {fahrenheit:.2f}°F")
