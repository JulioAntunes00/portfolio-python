#Peça ao usuário para digitar o valor de um produto e a porcentagem de desconto. Calcule e exiba o valor final com o desconto aplicado.

valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_final = valor - (valor * desconto / 100)

print(f"Valor com desconto: R$ {valor_final:.2f}")