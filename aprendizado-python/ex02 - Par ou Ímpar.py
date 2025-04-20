# Programa para verificar se um número é par ou ímpar

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é par (resto da divisão por 2 é 0)
if numero %2 == 0:
    print("O número é par")
else:
    print("O numero é impar")
