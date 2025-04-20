# Programa pra calcular o valor com desconto

# Pede o valor do produto
valor = float(input("Digite o valor do produto: "))

# Pede o percentual de desconto
desconto = float(input("Digite a porcentagem de desconto: "))

# Calcula o valor final com desconto aplicado
valor_final = valor - (valor * desconto / 100)

# Mostra o valor com desconto
print(f"Valor com desconto: R$ {valor_final:.2f}")
