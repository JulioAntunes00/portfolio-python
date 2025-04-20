# Programa que fica sorteando número até sair o 7 e aí ele para

import random

# Loop infinito
while True:
    # Sorteia um número de 1 a 10
    numero = random.randint(1,11)
    print(numero)
    # Se o número for 7, o loop é encerrado
    if numero == 7:
        break
