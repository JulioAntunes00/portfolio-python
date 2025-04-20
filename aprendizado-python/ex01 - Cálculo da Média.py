# Programa para calcular a média de três notas

# Solicita ao usuário que digite as três notas
nota1 = int(input("Digite sua nota 1: "))
nota2 = int(input("Digite sua note 2: "))
nota3 = int(input("Digite sua nota 3: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média com duas casas decimais
print(f"Sua média é de: {media:.2f}") 
