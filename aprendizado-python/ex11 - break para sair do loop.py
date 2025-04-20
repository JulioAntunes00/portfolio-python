#Escreva um código que utilize break para sair de um loop infinito quando um número aleatório entre 1 e 10 seja igual a 7.

import random

while True:
    numero = random.randint(1,11)
    print(numero)
    if numero == 7:
        break