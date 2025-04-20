#Crie um loop while que continue pedindo ao usuário para inserir uma palavra até que ele insira "sair".

while True:
    palavra = input("Insira uma palavra qualquer ou digite sair para encerrar:  ")
    if palavra == "sair":
        break