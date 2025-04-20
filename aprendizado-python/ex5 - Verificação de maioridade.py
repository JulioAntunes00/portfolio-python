#Peça ao usuário para inserir sua idade e informe se ele é maior ou menor de idade (considere 18 anos como maioridade).

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Parabéns, você é maior de idade!")
else:
    print("Você é menor de idade :(")
