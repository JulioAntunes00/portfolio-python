#Peça ao usuário para inserir o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula IMC = peso / 

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura * altura)

if imc >= 18.5 and imc <= 24.9:
    print(f"Seu IMC está bom: {imc:.2f}")
else:
    print(f"Seu IMC está ruim {imc:.2f}")
