# Programa que calcula a raiz quadrada de um número

import math

# Pede pro usuário digitar um número
numero = float(input("Digite um número: "))

# Usa a função sqrt do módulo math pra calcular a raiz
raiz = math.sqrt(numero)

# Mostra o resultado
print(f"A raiz quadrada de {numero} é {raiz:.2f}")
