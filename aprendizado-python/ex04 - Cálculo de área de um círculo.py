# Programa para calcular a área de um círculo

# Solicita o valor do raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Define o valor de pi
pi = 3.14159

# Calcula a área usando a fórmula A = π * r²
area = pi * (raio ** 2)

# Exibe a área formatada com duas casas decimais
print(f"A área do círculo é: {area:.2f}")
