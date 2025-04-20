# Programa que calcula o IMC da pessoa

# Pede o peso da pessoa
peso = float(input("Insira seu peso: "))

# Pede a altura
altura = float(input("Insira sua altura: "))

# Faz o cálculo do IMC
imc = peso / (altura * altura)

# Mostra se o IMC está dentro do normal ou não
if imc >= 18.5 and imc <= 24.9:
    print(f"Seu IMC está bom: {imc:.2f}")
else:
    print(f"Seu IMC está ruim {imc:.2f}")
