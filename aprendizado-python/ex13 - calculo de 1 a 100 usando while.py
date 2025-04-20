# Escreva um programa que use uma estrutura while para calcular a soma dos números de 1 a 100.

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    numero += 1

print(f"A soma é: {soma}")