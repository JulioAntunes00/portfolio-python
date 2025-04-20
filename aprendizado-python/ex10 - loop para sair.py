# Programa que fica rodando até o usuário digitar "sair"

while True:
    # Pede uma palavra
    palavra = input("Insira uma palavra qualquer ou digite sair para encerrar:  ")
    # Se for "sair", o programa para
    if palavra == "sair":
        break
